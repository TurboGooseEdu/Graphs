//
// Created by ilya on 20/05/22.
//

#include "UndirectedGraph.h"
UndirectedGraph::UndirectedGraph(std::string sourceFilename, std::string filename, int vertices)
    : Graph(sourceFilename, filename, vertices) {
    this->make();
}

void UndirectedGraph::addEdge(int u, int v) {
    this->addNode(u);
    this->addNode(v);
    simpleAddEdge(u, v);
}

void UndirectedGraph::simpleAddEdge(int u, int v) {
    if (this->adj[u].find(v) == this->adj[u].end()) {
        if (u != v)
            this->adj[v].insert(u);
        this->adj[u].insert(v);
        ++this->edges;
    }
}
void UndirectedGraph::removeNode(int u) {
    this->edges -= this->adj[u].size();
    for (auto v : this->adj[u]) {
        this->adj[v].erase(u);
    }
    this->adj[u].clear();
    --this->vertices;
}

void UndirectedGraph::removeEdge(int u, int v) {
    if (this->adj[u].find(v) == this->adj[u].end())
        return;
    this->adj[u].erase(v);
    this->adj[v].erase(u);
    --this->edges;
}

std::set<int> UndirectedGraph::getNeighbours(int v) {
    return this->adj[v];
}
