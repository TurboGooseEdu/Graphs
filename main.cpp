
#include <iostream>
#include <string>
#include <ctime>
#include "algorithms/graph.h"
#include "algorithms/basicAlgorithms.h"

/** Main function */
int main()
{

    clock_t t = clock();

    graph::Graph *astroGraph = new graph::Graph("data/CA-AstroPh.txt", "data/astro.txt");

    std::cout << "время обработки 1 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    graph::Graph *vkGraph = new graph::Graph("data/vk.csv", "data/vk.txt");
    std::cout << "время обработки 2 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    graph::Graph *googleGraph = new graph::Graph("data/web-Google.txt", "data/google.txt");
    std::cout << "время обработки 3 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    std::vector<graph::Graph *> graphs{
        astroGraph,
        vkGraph,
        googleGraph,
    };
    for (auto g : graphs)
    {
        int cc = graph::getConnectedComponents(*g);

        std::cout << "Количество компонент в графе " << g->getName() << ": " << cc << std::endl;
        std::cout << "Количество вершин: " << g->getVertices() << std::endl;

        std::cout << "Время подсчёта: " << (clock() - t) / 1e6 << " с." << std::endl;
        t = clock();
    }

    for (auto g : graphs)
    {
        delete g;
    }

    return 0;
}