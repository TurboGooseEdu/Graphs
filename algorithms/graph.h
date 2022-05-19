#ifndef ALGORITHMS_GRAPH_16_05_2022
#define ALGORITHMS_GRAPH_16_05_2022

#include <fstream>
#include <string>
#include <vector>
#include "../preprocess.h"

class Graph
{
private:
    std::string sourceName; // где хранится исходный датасет
    std::string name;       // где хранится преобразованный датасет
    int vertices;

    int getNumberVerticesFromFile(); // стрёмная функция, вообще говоря стоит это перенести куда-нибудь и сразу посчитать рёбра и т.п.
    void makeGraphFromFile();

public:
    Graph(std::string sourceFilename, std::string resultFilename);
    ~Graph();
    void addEdge(std::vector<std::vector<int>> *adj, int u, int v);
    std::vector<std::vector<int>> adj; // список смежности
    std::string getName();
    int getVertices();

}; // class graph::Graph

#endif
