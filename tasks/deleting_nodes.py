import random
from graph_impls.undirected_graph import UndirectedGraph
from tasks.degrees_and_plots import node_degrees
import copy


def select_random_nodes(graph: UndirectedGraph, number):
    # get list of pairs (node: adjacent_nodes_list)
    entry_list = list(graph.adj.items())

    random.shuffle(entry_list)

    # make list with nodes_numbers and cut from 0 to number
    return list(map(lambda item: item[0], entry_list))[:number]


def select_largest_degree_nodes(graph, number):
    # make dict with pairs (node_number : degree)
    nodes_degrees_dict = node_degrees(graph)
    # nodes_degrees_dict = dict(map(lambda item: (item[0], len(item[1])), graph.adj.items()))

    # sort node_degrees_dict in descending order
    largest_degree_nodes = dict(sorted(nodes_degrees_dict.items(), key=lambda item: item[1], reverse=True))

    # make list with dict keys and cut from 0 to number
    return list(map(lambda item: item[0], largest_degree_nodes.items()))[:number]


def delete_nodes(graph: UndirectedGraph, nodes):
    for node in nodes:
        graph.remove_node(node)

    return graph


def graph_deleted_random_nodes(graph, number):
    nodes = select_random_nodes(graph, number)

    return delete_nodes(copy.deepcopy(graph), nodes)


def graph_deleted_largest_nodes(graph, number):
    nodes = select_largest_degree_nodes(graph, number)

    return delete_nodes(copy.deepcopy(graph), nodes)
