from datasets.read_astro_dataset import read_astro_dataset
from datasets.read_google_dataset import read_google_dataset
from datasets.read_vk_dataset import read_vk_dataset
from graph_impls.undirected_graph import UndirectedGraph
from tasks.degrees_and_plots import node_degrees, average_node_degree, average_node_degree_from_graph, \
    degrees_probabilities, \
    probability_function_plot
import numpy as np
import matplotlib.pyplot as plt

from utils.random_graph import random_graph


def test_plots(array):
    figure = plt.figure()
    # fig, ax = plt.subplots(2, 1)
    # styles = plt.style.available

    ax1 = figure.add_subplot(2, 1, 1)
    ax2 = figure.add_subplot(2, 1, 2)

    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [9, 4, 1, 0, 1, 4, 9]

    # ax1.plot(x, y)
    ax1.plot(array)
    plt.loglog()
    ax2.plot(array)
    # ax2.plot(x, y)
    plt.show()


def init_graph(graph):
    graph.add_edge(1, 5)
    graph.add_edge(1, 8)
    graph.add_edge(1, 7)
    graph.add_edge(5, 8)
    graph.add_edge(7, 8)
    graph.add_edge(8, 4)
    graph.add_edge(8, 3)
    graph.add_edge(8, 6)
    graph.add_edge(7, 2)
    graph.add_edge(2, 6)
    graph.add_edge(6, 3)
    graph.add_edge(7, 5)
    graph.add_edge(2, 8)
    graph.add_edge(4, 7)
    graph.add_edge(2, 3)
    #
    # graph.add_edge(1, 2)
    # graph.add_edge(1, 3)
    # # graph.add_edge(2, 3)
    # graph.add_edge(1, 4)
    # graph.add_edge(2, 4)
    # graph.add_edge(4, 3)

    return graph


def test():
    # graph = init_graph(UndirectedGraph())
    # graph = random_graph(UndirectedGraph())
    # graph = read_astro_dataset('../datasets/CA-AstroPh.txt')
    # graph = read_google_dataset('../datasets/web-Google.txt')
    graph = read_vk_dataset('../../datasets/vk.csv')

    print(f'min degree {min(node_degrees(graph).values())}')
    print(f'max degree {max(node_degrees(graph).values())}')
    print(f'average degree {average_node_degree_from_graph(graph)}')
    # print(f'degrees probabilities {degrees_numbers(graph)}')
    # test_plots(degrees_numbers(graph))
    probability_function_plot(degrees_probabilities(graph))


if __name__ == '__main__':
    test()
