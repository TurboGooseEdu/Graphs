#ifndef UTILS_DFS_16_05_2022
#define UTILS_DFS_16_05_2022

#include <set>
#include <vector>

/**
 * @brief Utility function for depth first seach algorithm
 * this function explores the vertex which is passed into.
 *
 * @param adj adjacency list of graph.
 * @param u vertex or node to be explored.
 * @param visited already visited vertices.
 */
void DFS(std::vector<std::set<int>> *adj, int u, std::vector<bool> *visited);

#endif
