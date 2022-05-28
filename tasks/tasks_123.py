from random import sample
from typing import Union, List, Set, Tuple

from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph
from tasks.degrees import node_degrees, average_node_degree


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

    return output


def calculate_for_undirected_and_directed(undir_graph: UndirectedGraph, dir_graph: DirectedGraph) -> List[str]:
    output = calculate_for_undirected(undir_graph)
    scc = get_strongly_connected_components(dir_graph)
    max_scc = max(scc, key=lambda x: len(x))
    output.append("Число компонент сильной связности: " + str(len(scc)))
    output.append("Мощность максимальной компоненты сильной связности: " + str(len(max_scc)))
    output.append("Доля вершин в максимальной компоненте сильной связности: " + str(len(max_scc) / dir_graph.v))
    output.append(str(create_metagraph(dir_graph, scc)))
    return output


def create_metagraph(graph: DirectedGraph, components: List[Set[int]]) -> DirectedGraph:
    meta = DirectedGraph()
    for i in range(len(components)):
        meta.add_node(i)
        comp_adj_set = set()
        for v in components[i]:
            comp_adj_set = comp_adj_set.union(graph.adj[v])
        for j in range(len(components)):
            if i == j:
                continue
            if comp_adj_set.intersection(components[j]):
                meta.add_edge(i, j)
    return meta


def calculate_radius_diameter_percentile(graph: UndirectedGraph, verts: List[int], p: int = 90) -> Tuple[int, int, int]:
    ranges = []
    eccs = {v: -1 for v in verts}
    for i in range(len(verts) - 1):
        for j in range(i + 1, len(verts)):
            path_len = bfs(graph, verts[i], verts[j])
            eccs[verts[i]] = max(eccs[verts[i]], path_len)
            eccs[verts[j]] = max(eccs[verts[j]], path_len)
            ranges.append(path_len)
    eccs_values = eccs.values()
    radius = min(eccs_values)
    diameter = max(eccs_values)
    ranges.sort()
    percentile = ranges[p * len(ranges) // 100]
    return radius, diameter, percentile


def bfs(graph: UndirectedGraph, start: int, goal: int) -> int:
    if start == goal:
        return 0
    queue = [start, -1]
    visited = set()
    visited.add(start)
    level = 1
    while queue:
        s = queue.pop(0)
        if s == -1 and queue:
            level += 1
            queue.append(-1)
            continue
        for neighbour in graph.adj[s]:
            if neighbour == goal:
                return level
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return -1


def choose_x_random_vertices(verts: List[int], x: int) -> List[int]:
    if len(verts) < x:
        print("!!! Количество вершин в компоненте СС меньше {}: {}".format(x, len(verts)))
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
                for i in reversed(sort_sublist_in_list_order(graph.adj[v], order)):
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
    components = []
    posts = []
    for k in graph.adj.keys():
        if not visited[k]:
            component = set()
            stack = [k]
            while stack:
                v = stack.pop()
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
                    component.add(v)
                    for i in graph.adj[v]:
                        if not visited[i]:
                            stack.append(i)
                else:
                    if v not in posts:
                        posts.append(v)
            components.append(component)
    posts.reverse()
    return posts


def sort_sublist_in_list_order(sub: List[int], lst: List[int]) -> List[int]:
    res = []
    for i in lst:  # эта шняга работает за O(V) - все очень плохо...
        if i in sub:
            res.append(i)
        if len(res) == len(sub):
            break
    return res
