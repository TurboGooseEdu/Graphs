import copy
import random

from graph_impls import UndirectedGraph
from tasks import node_degrees
from tasks import get_weakly_connected_components
from tasks.plotting import plot_deleting_nodes


def get_random_nodes_list(graph: UndirectedGraph):
    # get list of pairs (node: adjacent_nodes_list)
    entry_list = list(graph.adj.items())

    random.shuffle(entry_list)

    # make list with nodes_numbers
    return list(map(lambda item: item[0], entry_list))


def get_largest_degree_nodes_list(graph):
    # make dict with pairs (node_number : degree)
    nodes_degrees_dict = node_degrees(graph)
    # nodes_degrees_dict = dict(map(lambda item: (item[0], len(item[1])), graph.adj.items()))

    # sort node_degrees_dict in descending order
    largest_degree_nodes = dict(sorted(nodes_degrees_dict.items(), key=lambda item: item[1], reverse=True))

    # make list with dict keys
    return list(map(lambda item: item[0], largest_degree_nodes.items()))


def delete_nodes_list(graph: UndirectedGraph, nodes):
    for node in nodes:
        graph.remove_node(node)

    return graph


def calculate_proportion_for_node(graph: UndirectedGraph, percentage: int):
    if graph.v == 0:
        print("Граф пуст")
        return 0

    output = []
    wcc = get_weakly_connected_components(graph)
    max_wcc = list(max(wcc, key=lambda x: len(x)))
    output.append("Название графа: " + str(graph.name))
    output.append("Удаляем " + str(percentage) + "%")
    output.append("Число вершин графа: " + str(graph.v))
    output.append("Число компонент слабой связности: " + str(len(wcc)))
    output.append("Мощность максимальной компоненты слабой связности: " + str(len(max_wcc)))
    output.append("Доля вершин в максимальной компоненте слабой связности: " + str(len(max_wcc) / graph.v))
    print(output)
    return len(max_wcc) / graph.v


def get_proportions_distribution(graph: UndirectedGraph, nodes):
    one_percent_nodes_number = graph.v // 100
    left_border = 0

    calculate_proportion_for_node(graph, 0)

    proportions = [0] * 100

    for i in range(100):
        right_border = left_border + one_percent_nodes_number
        delete_nodes_list(graph, nodes[left_border:right_border])

        proportions[i] = calculate_proportion_for_node(graph, i + 1)

        left_border = right_border

    return proportions


def create_nodes_proportions_graphs(graph):
    list_of_proportions = [
        get_proportions_distribution(copy.deepcopy(graph), get_random_nodes_list(graph)),
        get_proportions_distribution(graph, get_largest_degree_nodes_list(graph))
    ]

    plot_deleting_nodes(list_of_proportions, graph.name)
