from typing import List

from constants import DATASETS_OUTPUTS_FOLDER, DATASETS_FOLDER
from datasets.read_astro_dataset import read_astro_dataset
from datasets.read_google_dataset import read_google_dataset
from datasets.read_vk_dataset import read_vk_dataset
from graph_impls.undirected_graph import UndirectedGraph
from run_calculations import write_output_to_file
from tasks.degrees_and_plots import node_degrees, average_node_degree
from tasks.deleting_nodes import graph_deleted_random_nodes_percentage, graph_deleted_largest_nodes_percentage, \
    select_largest_degree_nodes
from tasks.triangles import triangles, local_clustering, average_clustering, all_clustering
from tasks.tasks_123 import get_weakly_connected_components
from utils.init_small_graph import init_graph_one


def calculate(graph: UndirectedGraph) -> List[str]:
    output = ["Граф: " + graph.name,
              "-" * 30,
              "Количество вершин: " + str(graph.v),
              "Количество ребер: " + str(graph.e)]

    print("clustering calculation")
    total_triangles, local_coeffs, average_coeff, global_coeff = all_clustering(graph)
    output.append("Количество треугольников: " + str(total_triangles))
    output.append("Средний кластерный коэффициент: " + str(average_coeff))
    output.append("Глобальный кластерный коэффициент: " + str(global_coeff))

    print("node_degrees calculation")
    degrees = node_degrees(graph)
    average_degree = average_node_degree(degrees)
    output.append(' ')
    output.append("Минимальная степень узла: " + str(min(degrees.values())))
    output.append("Максимальная степень узла: " + str(max(degrees.values())))
    output.append("Средняя степень узла: " + str(average_degree))

    print("weakly_connected_components calculation")
    wcc = get_weakly_connected_components(graph)
    max_wcc = list(max(wcc, key=lambda x: len(x)))
    output.append(' ')
    output.append("Число вершин графа: " + str(graph.v))
    output.append("Число компонент слабой связности: " + str(len(wcc)))
    output.append("Мощность максимальной компоненты слабой связности: " + str(len(max_wcc)))
    output.append("Доля вершин в максимальной компоненте слабой связности: " + str(len(max_wcc) / graph.v))

    print("10% random deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='random', percentage=10)]
    print("30% random deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='random', percentage=30)]
    print("50% random deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='random', percentage=50)]

    sorted_degree_nodes = select_largest_degree_nodes(graph, graph.v)

    print("10% largest deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='largest', percentage=10, nodes=sorted_degree_nodes)]
    print("30% largest deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='largest', percentage=30, nodes=sorted_degree_nodes)]
    print("50% largest deleting nodes calculation")
    output = [*output, *output_vertices_fraction(graph, func_type='largest', percentage=50, nodes=sorted_degree_nodes)]

    return output


def output_vertices_fraction(graph, func_type, percentage, nodes=None):
    new_graph: UndirectedGraph
    output = [' ']
    if percentage > 0:
        if func_type == "random":
            new_graph = graph_deleted_random_nodes_percentage(graph, percentage)
            func_type = " случайных "
        elif func_type == "largest":
            if nodes is None:
                new_graph = graph_deleted_largest_nodes_percentage(graph, percentage)
            else:
                new_graph = graph_deleted_largest_nodes_percentage(graph, percentage, nodes)
            func_type = " наибольших по степени "
        else:
            return
        output.append('Удаляем ' + str(percentage) + '%' + func_type + 'вершин')

    else:
        return

    wcc = get_weakly_connected_components(new_graph)
    max_wcc = list(max(wcc, key=lambda x: len(x)))
    output.append("Число вершин графа: " + str(new_graph.v))
    output.append("Число компонент слабой связности: " + str(len(wcc)))
    output.append("Мощность максимальной компоненты слабой связности: " + str(len(max_wcc)))
    output.append("Доля вершин в максимальной компоненте слабой связности: " + str(len(max_wcc) / new_graph.v))

    return output


def calculations():
    print("graph reading")
    # graph = init_graph_one(UndirectedGraph())
    graph = read_astro_dataset(DATASETS_FOLDER + 'CA-AstroPh.txt')
    # graph = read_google_dataset(DATASETS_FOLDER + 'web-Google.txt', UndirectedGraph)
    # graph = read_vk_dataset(DATASETS_FOLDER + 'vk.csv')
    # print(graph)

    output = calculate(graph)
    # write_output_to_file(DATASETS_OUTPUTS_FOLDER + 'test.txt', output)
    write_output_to_file(DATASETS_OUTPUTS_FOLDER + 'CA-AstroPh-output.txt', output)
    # write_output_to_file(DATASETS_OUTPUTS_FOLDER + 'web-Google-output.txt', output)
    # write_output_to_file(DATASETS_OUTPUTS_FOLDER + 'vk-output.txt', output)
    for string in output:
        print(string)

# if __name__ == '__main__':
#     calculations()

# sys.path.extend(['/home/pmikhail/projects/Graphs/']); from Graphs import *
