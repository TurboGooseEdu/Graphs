#include "Graph.h"

Graph::Graph(std::string filename, int vertices) {
    std::cout << "here1";
    this->name = filename;
    this->vertices = vertices;
    std::cout << "here2";
    this->adj = std::vector<std::set<int>>(vertices, std::set<int>());
    std::cout << "her3";
    // this->adjMatrix = std::vector<std::vector<bool>>(vertices, std::vector<bool>(vertices, false));
    std::cout << "here4" << std::endl;
    this->readfromFile();
}

Graph::~Graph() {}

void Graph::readfromFile() {
    std::ifstream in(this->name);
    std::string line;
    int count_edges = 0;

    if (!in.is_open()) {
        std::cout << "asa";
        return;
    }

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
std::string Graph::getName() const { return this->name.substr(7, this->name.length() - 11); }
int Graph::getVertices() const { return this->vertices; }
int Graph::getEdges() const { return this->edges; }
std::set<int> Graph::getNeighbours(int v) { return this->adj[v]; }
