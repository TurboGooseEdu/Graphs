//
// Created by ilya on 20/05/22.
//

#ifndef GRAPHS_UNDIRECTEDGRAPH_H
#define GRAPHS_UNDIRECTEDGRAPH_H

#include <iostream>
#include <map>
#include <set>

class UndirectedGraph {
    int vertices = 0;
    int edges = 0;

public:
    std::map<int, std::set<int>> adj;

    void add_edge(int u, int v);
    void remove_edge(int u, int v);
    void add_node(int n);
    void remove_node(int n);
    std::set<int> get_neighbours(int v);
    int get_vertices() const;
    int get_edges() const;
    void print();
};

#endif // GRAPHS_UNDIRECTEDGRAPH_H
