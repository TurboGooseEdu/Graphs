from utils.read_datasets import *
from tasks.tasks_123 import *
from tasks.deleting_nodes import *
from tasks.degrees_and_plots import *
from tasks.triangles import *
from utils.init_small_graph import *
from utils.random_graph import *


def write_output_to_file(output_filename: str, output: List[str]):
    with open(output_filename, "w") as out:
        for s in output:
            out.write(s + "\n")


def write_metagraph_to_file(output_filename: str, metagraph: DirectedGraph):
    with open(output_filename, "w") as out:
        for v in metagraph.adj:
            for u in metagraph.adj[v]:
                out.write(str(v) + " " + str(u) + "\n")


if __name__ == '__main__':
    available_graphs = [   # (directed, filename)
        (True, "datasets/email-Eu-core.txt"),
        (True, "datasets/soc-wiki-Vote.txt"),
        (False, "datasets/CA-GrQc.txt"),
        (False, "datasets/socfb-Middlebury45.txt"),
        (False, "datasets/socfb-Reed98.txt")
    ]

    graph_no = 1   # choose number of the graph from above
    directed, filename = available_graphs[graph_no]

    dir_graph, undir_graph = None, None
    if directed:
        undir_graph, dir_graph = read_undirected_and_directed_graphs(filename)
    else:
        undir_graph = read_undirected_graph(filename)

    # write your script here

