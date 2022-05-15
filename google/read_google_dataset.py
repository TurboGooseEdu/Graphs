from graph_impls.directed_graph import DirectedGraph


def read_google_dataset(filename, graph=None):
    if graph is None:
        graph = DirectedGraph()
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            node_from, node_to = line.split("\t")
            graph.add_edge(int(node_from), int(node_to))
    return graph
