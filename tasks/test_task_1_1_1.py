from tasks.task_1_1_1 import *


def test_undirected_graph():
    ug = UndirectedGraph()
    ug.add_edge(1, 2)
    ug.add_edge(1, 3)
    ug.add_edge(1, 5)
    ug.add_edge(2, 3)
    ug.add_edge(3, 4)
    ug.add_edge(5, 6)
    ug.add_edge(7, 8)
    ug.add_node(9)
    print(ug)
    calculate_task_1(ug)


def test_directed_graph():
    dg = DirectedGraph()
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 1)
    dg.add_edge(4, 3)
    dg.add_edge(5, 1)
    dg.add_edge(5, 6)
    dg.add_edge(6, 5)
    dg.add_edge(7, 8)
    dg.add_node(9)
    print(dg)
    calculate_task_1(dg)


if __name__ == '__main__':
    test_undirected_graph()
    print("\n" + "=" * 60 + "\n")
    test_directed_graph()
