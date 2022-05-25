from csv import reader

from graph_impls.undirected_graph import UndirectedGraph


def read_vk_dataset(filename):
    graph = UndirectedGraph("VK UndirectedGraph")
    with open(filename) as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            if not row[0].isdigit():
                continue
            node_from, node_to, *idk= row
            graph.add_edge(int(node_from), int(node_to))
    return graph
