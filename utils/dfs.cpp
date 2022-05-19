#include "dfs.h"

void DFS(const std::vector<std::vector<int>> *adj, int u, std::vector<bool> *visited)
{
    (*visited)[u] = true;
    for (auto v : (*adj)[u])
    {
        if (!(*visited)[v])
        {
            DFS(adj, v, visited);
        }
    }
}