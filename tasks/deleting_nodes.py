import copy
import random
from typing import List

from graph_impls import UndirectedGraph
from tasks import node_degrees
from datasets import read_astro_dataset, read_google_dataset, read_vk_dataset
from constants import DATASETS_FOLDER
from tasks import get_weakly_connected_components
import matplotlib.pyplot as plt
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


def calculate_fraction(graph: UndirectedGraph, percentage: int):
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


def calculate_all_fractions(graph: UndirectedGraph, nodes):
    one_percent_nodes_number = graph.v // 100
    left_border = 0

    calculate_fraction(graph, 0)

    proportions = [0] * 100

    for i in range(100):
        right_border = left_border + one_percent_nodes_number
        delete_nodes_list(graph, nodes[left_border:right_border])

        proportions[i] = calculate_fraction(graph, i + 1)

        left_border = right_border

    return proportions


def plot_nodes_fraction_graphs(graph):
    list_of_proportions = [
        calculate_all_fractions(copy.deepcopy(graph), get_random_nodes_list(graph)),
        calculate_all_fractions(graph, get_largest_degree_nodes_list(graph))
    ]

    plot_deleting_nodes(list_of_proportions, graph.name)


if __name__ == '__main__':
    # print('reading astro ph')
    # graph = read_astro_dataset(DATASETS_FOLDER + 'CA-AstroPh.txt')
    # plot_nodes_fraction_graphs(graph)

    print('reading web-google')
    graph = read_google_dataset(DATASETS_FOLDER + 'web-Google.txt', UndirectedGraph)
    plot_nodes_fraction_graphs(graph)
    #
    # print('reading vk')
    # graph = read_vk_dataset(DATASETS_FOLDER + 'vk.csv')
    # plot_nodes_fraction_graphs(graph)
