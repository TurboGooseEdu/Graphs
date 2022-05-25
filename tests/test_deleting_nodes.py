from datasets.read_astro_dataset import read_astro_dataset
from datasets.read_google_dataset import read_google_dataset
from datasets.read_vk_dataset import read_vk_dataset
from graph_impls.undirected_graph import UndirectedGraph
from tasks.deleting_nodes import select_random_nodes, select_largest_degree_nodes, graph_deleted_largest_nodes, \
    graph_deleted_random_nodes
from utils.init_small_graph import init_graph_one
from utils.random_graph import random_graph


def test():
    # graph = init_graph_one(UndirectedGraph())
    graph = random_graph(UndirectedGraph())
    # graph = read_astro_dataset('../../datasets/CA-AstroPh.txt')
    # graph = read_google_dataset('../../datasets/web-Google.txt')
    # graph = read_vk_dataset('../../../datasets/vk.csv')

    # print(graph)
    # print(select_random_nodes(graph, 2))
    print(select_largest_degree_nodes(graph, 6))

    # new_graph = graph_deleted_random_nodes(graph, 2)
    new_graph = graph_deleted_largest_nodes(graph, 3)

    # print(new_graph)
    print(select_largest_degree_nodes(new_graph, 3))


if __name__ == '__main__':
    test()
