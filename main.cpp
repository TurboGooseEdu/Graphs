#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <ctime>
#include <map>
#include <stack>

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
        // здесь "-1" везде, потому что нумерация вершин после препроцессинга от 1
        // а это в свою очередь было нужно из-за того, что вектор по умолчанию забивается нулями
        (*adj)[u - 1].push_back(v - 1);
        (*adj)[v - 1].push_back(u - 1);
    }

    std::vector<std::vector<int>> transposeGraph(const std::vector<std::vector<int>> *adj)
    {
        std::vector<std::vector<int>> transposed;
        for (int i = 0; i < adj->size(); i++)
            for (int j = 0; j < (*adj)[i].size(); j++)
                addEdge(&transposed, (*adj)[i][j], i);
        return transposed;
    }

    /**
     * @brief Utility function for depth first seach algorithm
     * this function explores the vertex which is passed into.
     *
     * @param adj adjacency list of graph.
     * @param u vertex or node to be explored.
     * @param visited already visited vertices.
     */
    void DFS(const std::vector<std::vector<int>> *adj, int u, std::vector<bool> *visited)
    {
        (*visited)[u] = true;
        for (auto v : (*adj)[u])
        {
            if (!(*visited)[v])
            {
                DFS(adj, v, visited);
            }
        }
    }

    /**
     * @brief нерекурсивный дфс на стеке, изменяет visited на месте
     *
     * @param adj список смежности
     * @param root вершина, от которой строим ДФС
     * @param visited массив bool, где храним метки посещена/не посещена вершина
     * @return ** void
     */
    void nonRecursiveDFS(const std::vector<std::vector<int>> *adj, int root, std::vector<bool> *visited)
    {
        (*visited)[root] = true;

        std::stack<int> s;
        s.push(root);

        while (!s.empty())
        {
            int u = s.top();

            (*visited)[u] = true;
            s.pop();

            for (auto v : (*adj)[u])
            {
                if (!(*visited)[v])
                    s.push(v);
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
    int getConnectedComponents(const std::vector<std::vector<int>> *adj, bool nonRecursive = false)
    {
        int n = adj->size();
        int connected_components = 0;
        std::vector<bool> visited(n, false);

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                if (nonRecursive)
                    nonRecursiveDFS(adj, i, &visited);
                else
                    DFS(adj, i, &visited);
                connected_components++;
            }
        }
        return connected_components;
    }
} // namespace graph

std::pair<int, int> parse_txt_line(std::string line)
{
    int u, v;
    std::istringstream iss(line);

    iss >> u;
    iss >> v;

    return std::make_pair(u, v);
}

std::pair<int, int> parse_csv_line(std::string line)
{
    int u, v;
    char colon;
    std::istringstream iss(line);

    iss >> u;
    iss >> colon;
    iss >> v;

    return std::make_pair(u, v);
}

/**
 * @brief Get the Number Vertices of graph in file
 *
 * @param filename
 * @return int
 */
int getNumberVertices(std::string filename)
{
    std::ifstream in(filename);
    std::string line;
    std::map<int, int> edges;

    int maxNumber = 0;

    if (in.is_open())
    {
        while (getline(in, line))
        {
            std::pair<int, int> vertices;
            vertices = parse_txt_line(line);

            int newMax = std::max(vertices.first, vertices.second);

            if (maxNumber < newMax)
                maxNumber = newMax;
        }
        in.close();
    }

    return maxNumber;
}
bool getIsTxt(std::string filename)
{
    return filename.substr(filename.find_last_of(".") + 1) == "txt";
}

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

    bool isTxt = getIsTxt(filename);

    std::map<int, int> edges;

    int count_vertices = 0; // ! номер первой вершины будет равен 1, не 0 !

    if (in.is_open() && out.is_open())
    {
        while (getline(in, line))
        {
            if (isdigit(line[0]))
            {
                std::pair<int, int> vertices;
                if (isTxt)
                    vertices = parse_txt_line(line);
                else
                    vertices = parse_csv_line(line);

                int u = vertices.first;
                int v = vertices.second;

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

    std::string sourceFilename;
    std::string filename;
    int NUMBER_VERTICES;

    sourceFilename = "local/CA-AstroPh.txt";
    filename = "local/astro.txt";

    // sourceFilename = "local/text.txt";
    // filename = "local/a.txt";

    // sourceFilename = "local/vk.csv";
    // filename = "local/vk.txt";

    preprocess(sourceFilename, filename);

    std::cout << "Время препроцессинга: " << (clock() - t) / 1e3 << " мс" << std::endl;
    t = clock();

    std::ifstream in(filename);
    std::string line;

    NUMBER_VERTICES = getNumberVertices(filename);

    std::cout << "NUMBER_VERTICES: " << NUMBER_VERTICES << std::endl;

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

    int cc;
    bool isVk = filename.find("vk") != std::string::npos;
    if (isVk)
        cc = graph::getConnectedComponents(&adj, true);
    else
        cc = graph::getConnectedComponents(&adj, false);

    std::cout << "Время подсчёта компонент: " << (clock() - t) / 1e3 << " мс" << std::endl
              << std::endl;

    std::cout << "Количество компонент: " << cc << std::endl;

    return 0;
}