#ifndef GRAPHS_GRAPH_16_05_2022
#define GRAPHS_GRAPH_16_05_2022

#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

class Graph {
private:
    std::string sourceName; // исходный датасет
    std::string name;       // преобразованный датасет
    int vertices;
    int edges;
    std::map<int, int> vertices_map;

public:
    Graph(std::string filename, int vertices);
    Graph(std::string filename);
    ~Graph();
    std::vector<std::set<int>> adj; // список смежности

    void preprocess(std::string filename);
    void readfromFile();
    void addEdge(int u, int v);
    int initial_vertex(int v);

    std::set<int> getNeighbours(int v);

    std::string getName() const;
    int getVertices() const;
    int getEdges() const;
};

#endif
