import time

from tasks.tasks_123 import calculate_for_undirected, calculate_for_directed
from datasets.read_vk_dataset import read_vk_dataset
from datasets.read_google_dataset import read_google_dataset_dir_and_undir
from datasets.read_astro_dataset import read_astro_dataset


def write_output_to_file(output_filename, output):
    with open(output_filename, "w") as out:
        for s in output:
            out.write(s + "\n")


def run_calculations_for_astro():
    astro = read_astro_dataset("/home/ilya/Programming/graph_data/CA-AstroPh.txt")
    print("reading completed")
    astro_output = calculate_for_undirected(astro)
    print("calculated")
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Astro-output.txt", astro_output)
    print("written to the file")


def run_calculations_for_vk():
    vk = read_vk_dataset("/home/ilya/Programming/graph_data/vk.csv")
    print("reading completed")
    vk_output = calculate_for_undirected(vk)
    print("calculated")
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/VK-output.txt", vk_output)
    print("written to the file")


def run_calculations_for_google():
    google_dir, google_undir = read_google_dataset_dir_and_undir("/home/ilya/Programming/graph_data/web-Google.txt")
    print("reading completed")
    undir_output = calculate_for_undirected(google_undir)
    print(undir_output)
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Google-undirected-output.txt", undir_output)

    dir_output = calculate_for_directed(google_dir)
    print(dir_output)
    metagraph = dir_output.pop()
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Google-directed-output.txt", dir_output)
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Google-metagraph.txt", metagraph)
    print("written to the file")


def calculate_time(process):
    start = time.time()
    print("Started in " + time.ctime(start))
    process()
    finish = time.time()
    print("Finished in " + time.ctime(finish))
    print("Elapsed time: " + str((finish - start) // 60))


if __name__ == '__main__':
    # calculate_time(run_calculations_for_astro)
    # calculate_time(run_calculations_for_google)
    calculate_time(run_calculations_for_vk)
