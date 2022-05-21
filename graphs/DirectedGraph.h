//
// Created by ilya on 20/05/22.
//

#ifndef GRAPHS_DIRECTEDGRAPH_H
#define GRAPHS_DIRECTEDGRAPH_H

#include "Graph.h"
#include <set>

class DirectedGraph : public Graph {
public:
    DirectedGraph(std::string sourceFilename, std::string filename);

    void addEdge(int u, int v);
    void simpleAddEdge(int u, int v);
    void removeNode(int n);
    void removeEdge(int u, int v);

    std::set<int> getOutcomingNeighbours(int v);
    std::set<int> getIncomingNeighbours(int v);
};

#endif // GRAPHS_DIRECTEDGRAPH_H
