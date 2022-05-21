//
// Created by ilya on 20/05/22.
//

#include "UndirectedGraph.h"

/**
 * @brief creates if not exists
 *
 * @param n номер вершины
 * @return ** void
 */
void UndirectedGraph::add_node(int n) {
    if (adj.count(n) == 0) {
        std::set<int> s;
        adj[n] = s;
        vertices++;
    }
}

void UndirectedGraph::remove_node(int n) {
    std::set<int> adj_n = adj[n];
    edges -= adj_n.size();
    for (auto node : adj_n) {
        adj[node].erase(n);
    }
    adj.erase(n);
    vertices--;
}

void UndirectedGraph::add_edge(int u, int v) {
    add_node(u);
    add_node(v);

    if (adj[u].find(v) == adj[u].end()) {
        if (u != v)
            adj[v].insert(u);
        adj[u].insert(v);
        edges++;
    }
}

void UndirectedGraph::remove_edge(int u, int v) {
    if (adj[u].find(v) == adj[u].end())
        return;

    adj[u].erase(v);
    adj[v].erase(u);
    edges--;
}

std::set<int> UndirectedGraph::get_neighbours(int v) {
    return adj[v];
}

int UndirectedGraph::get_vertices() const {
    return vertices;
}

int UndirectedGraph::get_edges() const {
    return edges;
}

void UndirectedGraph::print() {
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
