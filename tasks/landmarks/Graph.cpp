#include "Graph.h"

Graph::Graph(std::string filename, int vertices) {
    this->name = filename;
    this->vertices = vertices;
    this->adj = std::vector<std::set<int>>(vertices, std::set<int>());
    this->readfromFile();
}
Graph::Graph(std::string filename) {
    this->preprocess(filename);
    this->adj = std::vector<std::set<int>>(this->vertices, std::set<int>());
    this->readfromFile();
}

void Graph::preprocess(std::string sourceFilename) {
    std::ifstream in(sourceFilename);
    this->name = sourceFilename.substr(0, sourceFilename.length() - 4) + "-processed" + sourceFilename.substr(sourceFilename.length() - 4, sourceFilename.length());
    std::ofstream out(this->name);

    std::string line;
    std::map<int, int> edges;

    int count_vertices = 0;
    int count_edges = 0;

    if (!in.is_open() || !out.is_open())
        return;

    while (getline(in, line)) {
        int u, v;
        std::istringstream iss(line);
        iss >> u;
        iss >> v;
        if (edges[u] == 0)
            edges[u] = ++count_vertices;
        if (edges[v] == 0)
            edges[v] = ++count_vertices;

        out << edges[u] - 1 << " " << edges[v] - 1 << std::endl;
        ++count_edges;
    }

    this->edges = count_edges;
    this->vertices = count_vertices;
    this->vertices_map = edges;

    in.close();
    out.close();
}

void Graph::readfromFile() {
    std::ifstream in(this->name);
    std::string line;
    int count_edges = 0;

    if (!in.is_open())
        return;

    while (getline(in, line)) {
        int u, v;
        std::istringstream iss(line);
        iss >> u;
        iss >> v;
        this->addEdge(u, v);
        ++count_edges;
    }
    in.close();
    this->edges = count_edges;
}

void Graph::addEdge(int u, int v) {
    if (this->adj[u].find(v) != this->adj[u].end())
        return;
    if (u != v)
        this->adj[v].insert(u);
    this->adj[u].insert(v);
    ++this->edges;
}

Graph::~Graph() {}
int Graph::initial_vertex(int v) {
    return this->vertices_map[v] - 1;
}

std::string Graph::getName() const {
    return this->name.substr(7, this->name.length() - 11);
}
int Graph::getVertices() const { return this->vertices; }
int Graph::getEdges() const { return this->edges; }
std::set<int> Graph::getNeighbours(int v) { return this->adj[v]; }
