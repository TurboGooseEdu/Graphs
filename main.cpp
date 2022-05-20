//
// Created by ilya on 20/05/22.
//
#include "graphs/DirectedGraph.h"
#include "graphs/UndirectedGraph.h"
#include "iostream"

void test_undirected_graph();
void test_directed_graph();

int main() {
    test_undirected_graph();
    test_directed_graph();

    return 0;
}

void test_undirected_graph() {
    UndirectedGraph g;
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    g.add_edge(3, 1);
    g.add_edge(4, 5);
    g.print();

    for (auto n : g.get_neighbours(1))
        std::cout << n << " ";
    std::cout << std::endl;

    g.add_node(6);
    g.print();
    g.add_edge(6, 4);
    g.print();

    g.remove_edge(1, 2);
    g.print();
    g.remove_node(4);
    g.print();
}

void test_directed_graph() {
    DirectedGraph g;
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    g.add_edge(2, 2);
    g.add_edge(3, 1);
    g.add_edge(1, 3);
    g.add_edge(4, 5);
    g.print();

    for (auto n : g.get_incoming_neighbours(3))
        std::cout << n << " ";
    std::cout << std::endl;

    for (auto n : g.get_outcoming_neighbours(1))
        std::cout << n << " ";
    std::cout << std::endl;

    g.add_node(6);
    g.print();
    g.add_edge(6, 4);
    g.print();

    g.remove_edge(1, 2);
    g.print();
    g.remove_node(3);
    g.print();
}
