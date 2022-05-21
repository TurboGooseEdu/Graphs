#include <iostream>
#include <string>

#include "algorithms/basicAlgorithms.h"
#include "graphs/UndirectedGraph.h"

int main() {

    UndirectedGraph *astroGraph = new UndirectedGraph("data/CA-AstroPh.txt", "data/astro.txt", 18772);
    UndirectedGraph *vkGraph = new UndirectedGraph("data/vk.csv", "data/vk.txt", 3215722);
    UndirectedGraph *googleGraph = new UndirectedGraph("data/web-Google.txt", "data/google.txt", 875713);

    std::vector<UndirectedGraph *> graphs{
        astroGraph,
        vkGraph,
        googleGraph,
    };
    for (auto g : graphs) {
        int cc = getConnectedComponents(*g);

        std::cout << "Количество компонент в графе " << g->getName() << ": " << cc << std::endl;
        std::cout << "Количество вершин: " << g->getVertices() << std::endl;
        std::cout << "Количество рёбер: " << g->getEdges() << std::endl;
    }

    for (auto g : graphs)
        delete g;

    return 0;
}
