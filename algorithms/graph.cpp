#include "graph.h"

graph::Graph::Graph(std::string sourceFilename, std::string resultFilename)
{
    {
        this->sourceName = sourceFilename;
        this->name = resultFilename;
        // preprocess(sourceName, name);
        vertices = getNumberVerticesFromFile();
        makeGraphFromFile();
    }
}

int graph::Graph::getNumberVerticesFromFile()
{
    std::ifstream in(this->name);
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

void graph::Graph::addEdge(std::vector<std::vector<int>> *adj, int u, int v)
{
    // здесь "-1" везде, потому что нумерация вершин после препроцессинга от 1
    // а это в свою очередь было нужно из-за того, что вектор по умолчанию забивается нулями
    (*adj)[u - 1].push_back(v - 1);
    (*adj)[v - 1].push_back(u - 1); // todo вроде бы.... отсутствие этой строчки ничего не ломает...
}

void graph::Graph::makeGraphFromFile()
{
    std::ifstream in(name);
    std::string line;
    std::vector<std::vector<int>> adj(vertices, std::vector<int>());

    if (in.is_open())
    {
        while (getline(in, line))
        {
            std::pair<int, int> edge = parse_txt_line(line);
            addEdge(&adj, edge.first, edge.second);
        }
        this->adj = adj;
    }
    in.close();
}
std::string graph::Graph::getName()
{
    return this->name.substr(5, this->name.length() - 9);
}
graph::Graph::~Graph() {}

int graph::Graph::getVertices()
{
    return this->vertices;
}