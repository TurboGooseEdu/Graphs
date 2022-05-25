#ifndef GRAPHS_GRAPH_16_05_2022
#define GRAPHS_GRAPH_16_05_2022

#include "../utils/parse.h"
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

class Graph {
protected:
    std::string sourceName; // исходный датасет
    std::string name;       // преобразованный датасет
    int vertices;
    int edges;

public:
    Graph(std::string sourceFilename, std::string filename, int vertices);
    ~Graph();
    std::vector<std::set<int>> adj; // список смежности

    void make();

    void addNode(int u);
    virtual void addEdge(int u, int v) = 0;
    virtual void simpleAddEdge(int u, int v) = 0; // эта функция нужна для ускорения при парсинге
    virtual void removeNode(int n) = 0;
    virtual void removeEdge(int u, int v) = 0;

    std::string getName() const;
    int getVertices() const;
    int getEdges() const;
};

#endif
