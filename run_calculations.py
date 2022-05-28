import time

from tasks.tasks_123 import calculate_for_undirected, calculate_for_directed
from datasets.read_vk_dataset import read_vk_dataset
from datasets.read_google_dataset import read_google_dataset_dir_and_undir
from datasets.read_astro_dataset import read_astro_dataset


def write_output_to_file(output_filename, output):
    with open(output_filename, "w") as out:
        for s in output:
            out.write(s + "\n")


def write_metagraph_to_file(output_filename, metagraph):
    with open(output_filename, "w") as out:
        for v in metagraph.adj:
            for u in metagraph.adj[v]:
                out.write(str(v) + " " + str(u) + "\n")


def run_calculations_for_astro():
    astro = read_astro_dataset("/home/ilya/Programming/graph_data/CA-AstroPh.txt")
    print("Reading completed!")
    astro_output = calculate_for_undirected(astro)
    print("Calculations completed!")
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Astro-output.txt", astro_output)
    print("File saved!")


def run_calculations_for_vk():
    vk = read_vk_dataset("/home/ilya/Programming/graph_data/vk.csv")
    print("Reading completed!")
    vk_output = calculate_for_undirected(vk)
    print("Calculations completed!")
    write_output_to_file("/home/ilya/Programming/graph_data/outputs/VK-output.txt", vk_output)
    print("File saved!")


def run_calculations_for_google():
    google_dir, google_undir = read_google_dataset_dir_and_undir("/home/ilya/Programming/graph_data/web-Google.txt")
    print("Reading completed!")

    output = []
    output += calculate_for_undirected(google_undir)
    output += calculate_for_directed(google_dir)
    metagraph = output.pop()

    print("Calculations completed!")
    print()
    print(*output, sep="\n")
    print()

    write_output_to_file("/home/ilya/Programming/graph_data/outputs/Google-directed-output.txt", output)
    write_metagraph_to_file("/home/ilya/Programming/graph_data/outputs/Google-metagraph.txt", metagraph)
    print("File saved!")


def calculate_time(process):
    start = time.time()
    print("Started in " + time.ctime(start), end="\n\n")

    process()
    finish = time.time()

    print()
    print("Finished in " + time.ctime(finish))
    print("Elapsed time:", finish - start, "sec.")


if __name__ == '__main__':
    # calculate_time(run_calculations_for_astro)
    # calculate_time(run_calculations_for_google)
    calculate_time(run_calculations_for_vk)
