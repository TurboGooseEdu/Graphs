from typing import Union, List, Set, Dict

from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph


def calculate_stats_for_undirected_graph(graph: UndirectedGraph):
    print("Граф:", graph.name)
    print("-" * 30)
    print("Количество вершин:", graph.v)
    print("Количество ребер:", graph.e)
    print("Плотность графа:", calculate_density(graph))
    wcc = get_weakly_connected_components(graph)
    max_wcc = max(wcc, key=lambda x: len(x))
    print("Число компонент слабой связности:", len(wcc))
    print("Мощность максимальной компоненты слабой связности:", len(max_wcc))
    print("Доля вершин в максимальной компоненте слабой связности:", len(max_wcc) / graph.v)


def calculate_stats_for_directed_graph(graph: DirectedGraph):
    print("Граф:", graph.name)
    print("-" * 30)


def calculate_density(graph: Union[DirectedGraph, UndirectedGraph]) -> int:
    return 2 / (graph.e - 1)


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


def iterative_dfs_with_backtracking(graph: DirectedGraph) -> Dict[int, int]:
    visited = {k: False for k in graph.adj.keys()}
    components = []
    time = 0
    posts = {}
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
                        posts[v] = time
                        time += 1
            components.append(component)
    return posts


def transpose_graph(graph: DirectedGraph) -> DirectedGraph:
    transposed = DirectedGraph()
    for a in graph.adj.keys():
        for b in a:
            transposed.add_edge(b, a)
    return transposed


