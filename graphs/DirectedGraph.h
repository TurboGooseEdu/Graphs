//
// Created by ilya on 20/05/22.
//

#ifndef GRAPHS_DIRECTEDGRAPH_H
#define GRAPHS_DIRECTEDGRAPH_H

#include <iostream>
#include <map>
#include <set>

class DirectedGraph {
    int vertices = 0;
    int edges = 0;

public:
    std::map<int, std::set<int>> adj;

    void add_edge(int u, int v);
    void remove_edge(int u, int v);
    void add_node(int n);
    void remove_node(int n);
    std::set<int> get_outcoming_neighbours(int v);
    std::set<int> get_incoming_neighbours(int v);
    int get_vertices();
    int get_edges();
    void print();
};

#endif // GRAPHS_DIRECTEDGRAPH_H
