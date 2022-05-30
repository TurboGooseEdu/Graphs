from math import inf
from random import sample
from typing import Union, List, Set, Tuple

from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph
from tasks.degrees import node_degrees, average_node_degree
from tasks.clustering import all_clustering


def print_output(output):
    for s in output:
        print(s)


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

    total_triangles, local_coeffs, average_coeff, global_coeff = all_clustering(graph)
    output.append("Количество треугольников: " + str(total_triangles))
    output.append("Средний кластерный коэффициент: " + str(average_coeff))
    output.append("Глобальный кластерный коэффициент: " + str(global_coeff))

    degrees = node_degrees(graph)
    average_degree = average_node_degree(degrees)
    output.append(' ')
    output.append("Минимальная степень узла: " + str(min(degrees.values())))
    output.append("Максимальная степень узла: " + str(max(degrees.values())))
    output.append("Средняя степень узла: " + str(average_degree))

    wcc = get_weakly_connected_components(graph)
    max_wcc = list(max(wcc, key=lambda x: len(x)))
    output.append(' ')
    output.append("Число вершин графа: " + str(graph.v))
    output.append("Число компонент слабой связности: " + str(len(wcc)))
    output.append("Мощность максимальной компоненты слабой связности: " + str(len(max_wcc)))
    output.append("Доля вершин в максимальной компоненте слабой связности: " + str(len(max_wcc) / graph.v))

    print_output(output)

    return output


def calculate_for_directed(dir_graph: DirectedGraph) -> List[str]:
    output = []
    scc = get_strongly_connected_components(dir_graph)
    max_scc = max(scc, key=lambda x: len(x))
    output.append("Число компонент сильной связности: " + str(len(scc)))
    output.append("Мощность максимальной компоненты сильной связности: " + str(len(max_scc)))
    output.append("Доля вершин в максимальной компоненте сильной связности: " + str(len(max_scc) / dir_graph.v))
    output.append(str(create_metagraph(dir_graph, scc)))

    print_output(output)

    # output.append(create_metagraph(dir_graph, scc))
    return output


def print_calculations_for_undirected(graph: UndirectedGraph):
    print(*calculate_for_undirected(graph), sep="\n")


def print_calculations_for_directed(graph: DirectedGraph):
    print(*calculate_for_directed(graph), sep="\n")


# --------------------------------------------------------------------------------------------------------------------

def calculate_radius_diameter_percentile(graph: UndirectedGraph, verts: List[int]) -> Tuple[int, int, int]:
    ranges = []
    radius = inf
    diameter = -1
    goals = set(verts)
    for i in range(len(verts)):
        ecc, rngs = calculate_eccentricity_and_ranges(graph, verts[i], goals)
        merge_ranges_lists(ranges, rngs)
        radius = min(ecc, radius)
        diameter = max(ecc, diameter)
        p = calculate_percentile(ranges)
    percentile = calculate_percentile(ranges)
    return radius, diameter, percentile


def merge_ranges_lists(target: List[int], addition: List[int]):
    for i in range(min(len(target), len(addition))):
        target[i] += addition[i]
    if len(addition) > len(target):
        target += addition[len(target):]


def calculate_percentile(ranges: List[int], p: int = 90) -> int:
    n = sum(ranges)
    index = round(p * n / 100) - 1
    part_sum = 0
    for j in range(len(ranges)):
        if part_sum <= index < part_sum + ranges[j]:
            return j + 1
        part_sum += ranges[j]
    return -1


def calculate_eccentricity_and_ranges(graph: UndirectedGraph, start: int, goals: Set[int]) -> Tuple[int, List[int]]:
    ranges = [0]
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
            ranges.append(0)
            queue.append(-1)
            continue
        for neighbour in graph.adj[s]:
            if neighbour not in visited:
                if neighbour in goals:
                    ecc = max(ecc, level)
                ranges[-1] += 1
                visited.add(neighbour)
                queue.append(neighbour)
    ranges.pop()
    return ecc, ranges


def choose_x_random_vertices(verts: List[int], x: int) -> List[int]:
    return sample(verts, min(x, len(verts)))


def calculate_density(graph: Union[DirectedGraph, UndirectedGraph]) -> int:
    return 2 * graph.e / (graph.v - 1) / graph.v


def get_weakly_connected_components(graph: Union[DirectedGraph, UndirectedGraph]) -> List[Set[int]]:
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
    return components


def transpose_graph(graph: DirectedGraph) -> DirectedGraph:
    transposed = DirectedGraph()
    for v, adj in graph.adj.items():
        transposed.add_node(v)
        for u in adj:
            transposed.add_edge(u, v)
    return transposed


def iterative_dfs_with_backtracking(graph: DirectedGraph) -> List[int]:
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
    return posts
