//
// Created by ilya on 20/05/22.
//

#ifndef GRAPHS_UNDIRECTEDGRAPH_H
#define GRAPHS_UNDIRECTEDGRAPH_H

#include "Graph.h"
#include <iostream>
#include <set>

class UndirectedGraph : public Graph {
public:
    UndirectedGraph(std::string sourceFilename, std::string filename, int vertices);

    void addEdge(int u, int v);
    void simpleAddEdge(int u, int v);
    void removeNode(int n);
    void removeEdge(int u, int v);

    std::set<int> getNeighbours(int v);
};

#endif // GRAPHS_UNDIRECTEDGRAPH_H
