#include <iostream>
#include <string>
#include <ctime>
#include "algorithms/graph.h"
#include "algorithms/basicAlgorithms.h"

/** Main function */
int main()
{
    clock_t t = clock();

    Graph *astroGraph = new Graph("data/CA-AstroPh.txt", "data/astro.txt");

    std::cout << "время обработки 1 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    Graph *vkGraph = new Graph("data/vk.csv", "data/vk.txt");
    std::cout << "время обработки 2 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    Graph *googleGraph = new Graph("data/web-Google.txt", "data/google.txt");
    std::cout << "время обработки 3 " << (clock() - t) / 1e6 << " с." << std::endl;
    t = clock();

    std::vector<Graph *> graphs{
        astroGraph,
        vkGraph,
        googleGraph,
    };
    for (auto g : graphs)
    {
        int cc = getConnectedComponents(*g);

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
