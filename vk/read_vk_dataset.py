from graph_impls.undirected_graph import UndirectedGraph
from graph_impls.undirected_weighted_graph import UndirectedWeightedGraph
from csv import reader


def read_google_dataset_as_undirected_weighted_graph(filename):
    graph = UndirectedWeightedGraph()
    with open(filename) as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            if not row[0].isdigit():
                continue
            node_from, node_to, *idk = row
            graph.add_edge(int(node_from), int(node_to), 1)
    return graph


def read_google_dataset_as_undirected_graph(filename):
    graph = UndirectedGraph()
    with open(filename) as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            if not row[0].isdigit():
                continue
            node_from, node_to, *_ = row
            graph.add_edge(int(node_from), int(node_to))
    return graph
