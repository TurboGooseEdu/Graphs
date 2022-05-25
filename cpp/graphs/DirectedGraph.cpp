//
// Created by ilya on 20/05/22.
//

#include "DirectedGraph.h"

DirectedGraph::DirectedGraph(std::string sourceFilename, std::string filename)
    : Graph(sourceFilename, filename, vertices) {
    this->make();
}

void DirectedGraph::addEdge(int u, int v) {

    this->addNode(u);
    this->addNode(v);
    simpleAddEdge(u, v);
}

void DirectedGraph::simpleAddEdge(int u, int v) {
    if (this->adj[u].find(v) == this->adj[u].end()) {
        this->adj[u].insert(v);
        this->edges++;
    }
};

void DirectedGraph::removeNode(int u) {
    this->edges -= this->adj[u].size();
    for (int v = 0; v < this->getVertices(); ++v) {
        if (this->adj[v].find(u) != this->adj[v].end()) {
            this->adj[v].erase(u);
            this->edges--;
        }
    }
    this->adj[u].clear();
    --this->vertices;
}

void DirectedGraph::removeEdge(int u, int v) {
    if (this->adj[u].find(v) == this->adj[u].end())
        return;
    this->adj[u].erase(v);
    this->edges--;
}

std::set<int> DirectedGraph::getIncomingNeighbours(int v) {
    std::set<int> incoming;
    for (int u = 0; u < this->getVertices(); ++u) {
        if (this->adj[u].find(v) != this->adj[u].end()) {
            incoming.insert(u);
        }
    }
    return incoming;
}

std::set<int> DirectedGraph::getOutcomingNeighbours(int v) {
    return this->adj[v];
}
