#include "dfs.h"

void DFS(std::vector<std::set<int>> *adj, int u, std::vector<bool> *visited) {
    (*visited)[u] = true;

    for (auto v : (*adj)[u]) {
        if (!(*visited)[v]) {
            DFS(adj, v, visited);
        }
    }
}
