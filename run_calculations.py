import networkx as nx
import numpy as np

from datasets.read_google_dataset import read_google_dataset_dir_and_undir, read_google_dataset
from datasets.read_astro_dataset import read_astro_dataset
from datasets.read_vk_dataset import read_vk_dataset
from tasks import calculate_for_undirected, calculate_for_undirected_and_directed
from constants import *


def write_output_to_file(output_filename, output):
    with open(output_filename, "w") as out:
        for s in output:
            out.write(s + "\n")


def run_calculations_for_astro():
    astro = read_astro_dataset(DATASETS_FOLDER + 'CA-AstroPh.txt')

    astro_output = calculate_for_undirected(astro)
    write_output_to_file(DATASETS_OUTPUTS_FOLDER + "Astro-output.txt", astro_output)


def run_calculations_for_vk():
    vk = read_vk_dataset(DATASETS_FOLDER + 'vk.csv')
    vk_output = calculate_for_undirected(vk)
    write_output_to_file(DATASETS_OUTPUTS_FOLDER + "VK-output.txt", vk_output)


def run_calculations_for_google():
    google_dir, google_undir = read_google_dataset_dir_and_undir(DATASETS_FOLDER + 'web-Google.txt')
    google_output = calculate_for_undirected_and_directed(google_undir, google_dir)
    metagraph = google_output.pop()
    write_output_to_file(DATASETS_OUTPUTS_FOLDER + WEB_GOOGLE_OUTPUT_FILE, google_output)
    write_output_to_file(DATASETS_OUTPUTS_FOLDER + GOOGLE_METAGRAPH, metagraph)


if __name__ == '__main__':
    pass
    # run_calculations_for_astro()
    # run_calculations_for_google()
    # run_calculations_for_vk()
