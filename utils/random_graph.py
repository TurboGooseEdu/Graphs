import random


def random_graph(graph, v=1000, e=10000):
    for i in range(e):
        a = random.randint(1, v)
        b = random.randint(1, v)

        while a == b:
            b = random.randint(1, v)

        graph.add_edge(a, b)
    return graph
