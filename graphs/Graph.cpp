#include "Graph.h"

Graph::Graph(std::string sourceFilename, std::string filename, int vertices) {
    this->sourceName = sourceFilename;
    this->name = filename;
    this->vertices = vertices;
    std::vector<std::set<int>> adj = std::vector<std::set<int>>(vertices, std::set<int>());
    this->adj = adj;
}
Graph::~Graph() {}

void Graph::make() {
    std::ifstream in(this->sourceName);
    std::ofstream out(this->name);

    std::string line;
    std::map<int, int> edges;

    bool isCSV = this->sourceName.find("csv") != std::string::npos;
    int count_vertices = 0;
    int count_edges = 0;

    if (!in.is_open() || !out.is_open())
        return;

    while (getline(in, line)) {
        std::pair<int, int> edge;
        if (isCSV)
            edge = parse_csv_line(line);
        else
            edge = parse_txt_line(line);

        int u = edge.first;
        int v = edge.second;
        if (edges[u] == 0)
            edges[u] = ++count_vertices;
        if (edges[v] == 0)
            edges[v] = ++count_vertices;

        this->simpleAddEdge(edges[u] - 1, edges[v] - 1);
        out << edges[u] - 1 << " " << edges[v] - 1 << std::endl;
        ++count_edges;
    }

    if (this->vertices != count_vertices) {
        std::cout << "Вершин получилось чуть меньше: ";
        std::cout << count_vertices << std::endl;
    };

    this->edges = count_edges;

    in.close();
    out.close();
}

void Graph::addNode(int u) {
    this->vertices++;
}

std::string Graph::getName() const { return this->name.substr(5, this->name.length() - 9); }
int Graph::getVertices() const { return this->vertices; }
int Graph::getEdges() const { return this->edges; }

//-----------------------------------------------------------

std::ostream &operator<<(std::ostream &out, const Graph &g) {

    for (int i = 0; i < 7; ++i) {
        out << "(" << i << ") -> [";

        for (auto v : g.adj[i]) {
            out << v << ", ";
        }
        if (g.adj[i].size() != 0) {
            out << "\b \b\b \b";
        }
        out << "]" << std::endl;
    }
    out << "V: " << g.getVertices() << ", E: " << g.getEdges() << std::endl;

    return out;
}
