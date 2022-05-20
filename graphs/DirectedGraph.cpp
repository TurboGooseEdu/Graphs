//
// Created by ilya on 20/05/22.
//

#include "DirectedGraph.h"
#include "iostream"

void DirectedGraph::add_node(int n) {
    if (adj.count(n) == 0) {
        std::set<int> s;
        adj[n] = s;
        vertices++;
    }
}

void DirectedGraph::remove_node(int n) {
    edges -= adj[n].size();
    for (std::pair<int, std::set<int>> p : adj) {
        if (p.second.find(n) != p.second.end()) {
            adj[p.first].erase(n);
            edges--;
        }
    }
    adj.erase(n);
    vertices--;
}

void DirectedGraph::add_edge(int u, int v) {
    add_node(u);
    add_node(v);
    if (adj[u].find(v) == adj[u].end()) {
        adj[u].insert(v);
        edges++;
    }
}

void DirectedGraph::remove_edge(int u, int v) {
    if (adj[u].find(v) != adj[u].end()) {
        adj[u].erase(v);
        edges--;
    }
}

std::set<int> DirectedGraph::get_incoming_neighbours(int v) {
    std::set<int> incoming;
    for (std::pair<int, std::set<int>> p : adj) {
        if (p.second.find(v) != p.second.end()) {
            incoming.insert(p.first);
        }
    }
    return incoming;
}

std::set<int> DirectedGraph::get_outcoming_neighbours(int v) {
    return adj[v];
}


int DirectedGraph::get_vertices() {
    return vertices;
}

int DirectedGraph::get_edges() {
    return edges;
}

void DirectedGraph::print() {
    for (std::pair<int, std::set<int>> p : adj) {
        std::cout << "(" << p.first << ") -> [";

        for (auto v : p.second) {
            std::cout << v << ", ";
        }
        if (p.second.size() != 0) {
            std::cout << "\b \b\b \b";
        }
        std::cout << "]" << std::endl;
    }
    std::cout << "V: " << vertices << ", E: " << edges << std::endl;
}
