from graph_impls.undirected_graph import UndirectedGraph
from graph_impls.directed_graph import DirectedGraph

def test_directed():
    dg = DirectedGraph()
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 4)
    dg.add_edge(5, 2)
    dg.add_edge(5, 4)
    print(dg)

    dg.add_edge(1, 15)
    dg.add_edge(4, 5)
    dg.add_node(20)
    print(dg)

    print(dg.incoming_neighbours(4))
    print(dg.outcoming_neighbours(2))

    dg.remove_edge(3, 4)
    print(dg)

    dg.remove_node(2)
    print(dg)


def test_undirected():
    ug = UndirectedGraph()
    ug.add_edge(1, 2)
    ug.add_edge(2, 3)
    ug.add_edge(2, 4)
    ug.add_edge(3, 4)
    ug.add_edge(5, 2)
    ug.add_edge(5, 4)
    print(ug)

    ug.add_edge(1, 15)
    ug.add_edge(4, 5)
    ug.add_node(20)
    print(ug)

    print(ug.node_neighbours(2))

    ug.remove_edge(3, 4)
    print(ug)

    ug.remove_node(2)
    print(ug)


if __name__ == '__main__':
    test_directed()
    test_undirected()
