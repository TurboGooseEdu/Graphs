#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <ctime>
#include <map>

/**
 * @namespace graph
 * @brief Graph Algorithms
 */

namespace graph
{

    /**
     * @brief Function that add edge between two nodes or vertices of graph
     *
     * @param adj adjacency list of graph.
     * @param u any node or vertex of graph.
     * @param v any node or vertex of graph.
     */
    void addEdge(std::vector<std::vector<int>> *adj, int u, int v)
    {
        (*adj)[u - 1].push_back(v - 1);
        (*adj)[v - 1].push_back(u - 1);
    }

    /**
     * @brief Utility function for depth first seach algorithm
     * this function explores the vertex which is passed into.
     *
     * @param adj adjacency list of graph.
     * @param u vertex or node to be explored.
     * @param visited already visited vertices.
     */
    void explore(const std::vector<std::vector<int>> *adj, int u,
                 std::vector<bool> *visited)
    {
        (*visited)[u] = true;
        for (auto v : (*adj)[u])
        {
            if (!(*visited)[v])
            {
                explore(adj, v, visited);
            }
        }
    }

    /**
     * @brief Function that perfoms depth first search algorithm on graph
     * and calculated the number of connected components.
     *
     * @param adj adjacency list of graph.
     *
     * @return connected_components number of connected components in graph.
     */
    int getConnectedComponents(const std::vector<std::vector<int>> *adj)
    {
        int n = adj->size();
        int connected_components = 0;
        std::vector<bool> visited(n, false);

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                explore(adj, i, &visited);
                connected_components++;
            }
        }
        return connected_components;
    }
} // namespace graph

/**
 * @brief Просматривает строчки начинающиеся с цифры.
 * Отображает номера вершин в множество [1, V], где V - кол-во вершин.
 * Преобразование сохраняет структуру графа.
 *
 * Например граф [(100, 18), (18, 2000), (34, 100), (1700, 1700)] преобразуется в [(1, 2), (2, 3), (4, 1), (5, 5)].
 *
 * Cохраняет преобразованный файл в файл с новым названием.
 *
 * @param filename имя исходного "грязного" файла
 * @param outputFilename имя нового "чистого" файла
 *
 * @author egorgorban
 */
void preprocess(std::string filename, std::string outputFilename)
{
    std::ifstream in(filename);
    std::ofstream out(outputFilename);
    std::string line;

    std::map<int, int> edges;
    int u, v;

    int count_vertices = 0; // ! номер первой вершины будет равен 1, не 0 !

    if (in.is_open() && out.is_open())
    {
        while (getline(in, line))
        {
            if (isdigit(line[0]))
            {
                std::istringstream iss(line);

                iss >> u;
                iss >> v;

                std::cout << u << v << std::endl;

                if (edges[u] == 0)
                    edges[u] = ++count_vertices;
                if (edges[v] == 0)
                    edges[v] = ++count_vertices;

                out << edges[u] << " " << edges[v] << std::endl;
            }
        }
        in.close();
        out.close();
    }
}

/** Main function */
int main()
{

    clock_t t = clock();

    std::string filename = "CA-AstroPh.txt";
    int NUMBER_VERTICES = 18772;

    preprocess(filename, "astro.txt");

    std::cout << "Время препроцессинга: " << (clock() - t) / 1e3 << " мс" << std::endl;
    t = clock();

    std::ifstream in("a.txt");
    std::string line;

    std::vector<std::vector<int>> adj(NUMBER_VERTICES, std::vector<int>());
    int u, v;

    if (in.is_open())
    {
        while (getline(in, line))
        {
            std::istringstream iss(line);

            iss >> u;
            iss >> v;

            graph::addEdge(&adj, u, v);
        }
    }

    std::cout << "Время делания графа: " << (clock() - t) / 1e3 << " мс" << std::endl;
    t = clock();
    int cc = graph::getConnectedComponents(&adj);

    std::cout << "Время подсчёта компонент: " << (clock() - t) / 1e3 << " мс" << std::endl
              << std::endl;

    std::cout << "Количество компонент: " << cc << std::endl;

    return 0;
}