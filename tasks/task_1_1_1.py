from typing import Union, List, Set

from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph


def calculate_task_1(graph: Union[DirectedGraph, UndirectedGraph]):
    if type(graph) is UndirectedGraph:
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

    if type(graph) is DirectedGraph:
        scc = get_strongly_connected_components(graph)
        max_scc = max(scc, key=lambda x: len(x))
        print("Число компонент сильной связности:", len(scc))
        print("Мощность максимальной компоненты сильной связности:", len(max_scc))
        print("Доля вершин в максимальной компоненте сильной связности:", len(max_scc) / graph.v)


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
    for i in lst:    # эта шняга работает за O(V) - все очень плохо...
        if i in sub:
            res.append(i)
        if len(res) == len(sub):
            break
    return res

