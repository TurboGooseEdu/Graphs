from _csv import reader

from graph_impls.undirected_graph import UndirectedGraph
from graph_impls.directed_graph import DirectedGraph
from typing import *
import re


def read_undirected_graph(filename: str) -> UndirectedGraph:
    graph = UndirectedGraph(filename[filename.rfind("/") + 1: filename.rfind(".")] + " UndirectedGraph")
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            node_from, node_to = re.split(" |\t", line)
            graph.add_edge(int(node_from), int(node_to))
    return graph


def read_undirected_and_directed_graphs(filename: str) -> Tuple[UndirectedGraph, DirectedGraph]:
    dir_graph = DirectedGraph(filename[filename.rfind("/") + 1: filename.rfind(".")])
    undir_graph = UndirectedGraph(filename[filename.rfind("/") + 1: filename.rfind(".")])
    with open(filename) as file:
        for line in file:
            if line.startswith("#"):
                continue
            node_from, node_to = re.split(" |\t", line)
            dir_graph.add_edge(int(node_from), int(node_to))
            undir_graph.add_edge(int(node_from), int(node_to))
    return undir_graph, dir_graph


def read_undirected_graph_csv(filename: str) -> UndirectedGraph:
    graph = UndirectedGraph(filename[filename.rfind("/") + 1: filename.rfind(".")] + " UndirectedGraph")
    with open(filename) as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            if not row[0].isdigit():
                continue
            node_from, node_to, *idk = row
            graph.add_edge(int(node_from), int(node_to))
    return graph
