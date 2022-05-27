def init_graph_one(graph):
    graph.add_edge(1, 5)
    graph.add_edge(1, 8)
    graph.add_edge(1, 7)
    graph.add_edge(5, 8)
    graph.add_edge(7, 8)
    graph.add_edge(8, 4)
    graph.add_edge(8, 3)
    graph.add_edge(8, 6)
    graph.add_edge(7, 2)
    graph.add_edge(2, 6)
    graph.add_edge(6, 3)
    graph.add_edge(7, 5)
    graph.add_edge(2, 8)
    graph.add_edge(4, 7)
    graph.add_edge(2, 3)

    return graph


def init_graph_two(graph):
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    # graph.add_edge(2, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(4, 3)

    return graph
