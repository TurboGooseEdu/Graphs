from tasks.tasks_123 import calculate_for_undirected, calculate_for_undirected_and_directed
from datasets.read_vk_dataset import read_vk_dataset
from datasets.read_google_dataset import read_google_dataset_dir_and_undir
from datasets.read_astro_dataset import read_astro_dataset


def write_output_to_file(output_filename, output):
    with open(output_filename, "w") as out:
        for s in output:
            out.write(s + "\n")


def run_calculations_for_astro():
    astro = read_astro_dataset("~/Programming/graph_data/CA-AstroPh.txt")
    astro_output = calculate_for_undirected(astro)
    write_output_to_file("~/Programming/graph_data/Astro-output.txt", astro_output)


def run_calculations_for_vk():
    vk = read_vk_dataset("~/Programming/graph_data/vk.csv")
    vk_output = calculate_for_undirected(vk)
    write_output_to_file("~/Programming/graph_data/VK-output.txt", vk_output)


def run_calculations_for_google():
    google_dir, google_undir = read_google_dataset_dir_and_undir("~/Programming/graph_data/web-Google.txt")
    google_output = calculate_for_undirected_and_directed(google_undir, google_dir)
    metagraph = google_output.pop()
    write_output_to_file("~/Programming/graph_data/outputs/Google-output.txt", google_output)
    write_output_to_file("~/Programming/graph_data/outputs/Google-metagraph.txt", metagraph)


if __name__ == '__main__':
    pass
    # run_calculations_for_astro()
    # run_calculations_for_google()
    # run_calculations_for_vk()
