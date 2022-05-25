from graph_impls.undirected_graph import UndirectedGraph


def read_astro_dataset(filename):
    graph = UndirectedGraph("Astro UndirectedGraph")
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            node_from, node_to = line.split("\t")
            graph.add_edge(int(node_from), int(node_to))
    return graph
