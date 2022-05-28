from math import inf
from random import sample
from typing import Union, List, Set, Tuple

from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph


def calculate_for_undirected(graph: UndirectedGraph) -> List[str]:
    output = []
    output.append("Граф: " + graph.name)
    output.append("-" * 30)
    output.append("Количество вершин: " + str(graph.v))
    output.append("Количество ребер: " + str(graph.e))
    output.append("Плотность графа: " + str(calculate_density(graph)))
    wcc = get_weakly_connected_components(graph)
    max_wcc = list(max(wcc, key=lambda x: len(x)))
    output.append("Число компонент слабой связности: " + str(len(wcc)))
    output.append("Мощность максимальной компоненты слабой связности: " + str(len(max_wcc)))
    output.append("Доля вершин в максимальной компоненте слабой связности: " + str(len(max_wcc) / graph.v))

    wcc_part = choose_x_random_vertices(max_wcc, 500)
    r, d, p = calculate_radius_diameter_percentile(graph, wcc_part)
    output.append("Радиус наибольшей компоненты слабой связности: " + str(r))
    output.append("Диаметр наибольшей компоненты слабой связности: " + str(d))
    output.append("90 процентиль расстояния между вершинами графа: " + str(p))
    return output


def calculate_for_directed(dir_graph: DirectedGraph) -> List[str]:
    output = []
    scc = get_strongly_connected_components(dir_graph)
    max_scc = max(scc, key=lambda x: len(x))
    output.append("Число компонент сильной связности: " + str(len(scc)))
    output.append("Мощность максимальной компоненты сильной связности: " + str(len(max_scc)))
    output.append("Доля вершин в максимальной компоненте сильной связности: " + str(len(max_scc) / dir_graph.v))
    output.append(create_metagraph(dir_graph, scc))
    return output


def calculate_radius_diameter_percentile(graph: UndirectedGraph, verts: List[int], p: int = 90) -> Tuple[int, int, int]:
    print("Start calculating radius and diameter")
    ranges = []
    radius = inf
    diameter = -1
    goals = set(verts)
    for v in verts:
        ecc, rngs = calculate_eccentricity_and_ranges(graph, v, goals)
        ranges += rngs
        radius = min(ecc, radius)
        diameter = max(ecc, diameter)
    ranges.sort()
    percentile = ranges[p * len(ranges) // 100]
    print("Finish calculating radius and diameter")
    return radius, diameter, percentile


def calculate_eccentricity_and_ranges(graph: UndirectedGraph, start: int, goals: Set[int]) -> Tuple[int, List[int]]:
    ranges = []
    ecc = -1
    queue = [start, -1]
    visited = set()
    visited.add(start)
    level = 1
    while queue:
        s = queue.pop(0)
        if s == -1:
            if not queue:
                break
            level += 1
            queue.append(-1)
            continue
        for neighbour in graph.adj[s]:
            if neighbour not in visited:
                if neighbour in goals:
                    ecc = max(ecc, level)
                ranges.append(level)
                visited.add(neighbour)
                queue.append(neighbour)
    return ecc, ranges


def choose_x_random_vertices(verts: List[int], x: int) -> List[int]:
    if len(verts) < x:
        print("!!! Количество вершин в компоненте СС меньше {}: {}".format(x, len(verts)))
    return sample(verts, min(x, len(verts)))


def calculate_density(graph: Union[DirectedGraph, UndirectedGraph]) -> int:
    return 2 / (graph.e - 1)


def get_weakly_connected_components(graph: Union[DirectedGraph, UndirectedGraph]) -> List[Set[int]]:
    print("Calculating weakly connected components...")
    components = []
    visited = {k: False for k in graph.adj.keys()}
    for k in graph.adj.keys():
        if not visited[k]:
            component = set()
            stack = [k]
            while stack:
                v = stack.pop()
                visited[v] = True
                component.add(v)
                for i in graph.adj[v]:
                    if not visited[i]:
                        stack.append(i)
            components.append(component)
    print("Weakly connected components calculated!")
    return components


def create_metagraph(graph: DirectedGraph, components: List[Set[int]]) -> DirectedGraph:
    vert_scc = {}
    for i in range(len(components)):
        for v in components[i]:
            vert_scc[v] = i
    metagraph = DirectedGraph()
    for v in graph.adj:
        metagraph.add_node(vert_scc[v])
        for u in graph.adj[v]:
            if vert_scc[v] != vert_scc[u]:
                metagraph.add_edge(vert_scc[v], vert_scc[u])
    return metagraph


def get_strongly_connected_components(graph: DirectedGraph) -> List[Set[int]]:
    print("Calculating strongly connected components...")
    order = iterative_dfs_with_backtracking(transpose_graph(graph))
    components = []
    visited = {k: False for k in graph.adj.keys()}
    for k in order:
        if not visited[k]:
            component = set()
            stack = [k]
            while stack:
                v = stack.pop()
                visited[v] = True
                component.add(v)
                for i in graph.adj[v]:
                    if not visited[i]:
                        stack.append(i)
            components.append(component)
    print("Strongly connected components calculated!")
    return components


def transpose_graph(graph: DirectedGraph) -> DirectedGraph:
    print("Transposing graph...")
    transposed = DirectedGraph()
    for v, adj in graph.adj.items():
        transposed.add_node(v)
        for u in adj:
            transposed.add_edge(u, v)
    print("Transposed!")
    return transposed


def iterative_dfs_with_backtracking(graph: DirectedGraph) -> List[int]:
    print("Performing DFS with backtracking...")
    visited = {k: False for k in graph.adj.keys()}
    posts = []
    posts_check = set()
    for k in graph.adj.keys():
        if not visited[k]:
            stack = [k]
            while stack:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    for i in graph.adj[v]:
                        if not visited[i]:
                            stack.append(i)
                else:
                    if v not in posts_check:
                        posts.append(v)
                        posts_check.add(v)
    posts.reverse()
    print("DFS completed!")
    return posts
