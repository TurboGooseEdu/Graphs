from graph_impls.directed_graph import DirectedGraph
from graph_impls.undirected_graph import UndirectedGraph


def read_google_dataset(filename, graph_type=DirectedGraph):
    graph = graph_type("Google " + graph_type.__class__.__name__)
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            node_from, node_to = line.split("\t")
            graph.add_edge(int(node_from), int(node_to))
    return graph


def read_google_dataset_dir_and_undir(filename):
    return read_google_dataset(filename), read_google_dataset(filename, UndirectedGraph)
