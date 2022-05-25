#ifndef UTILS_STACK_DFS_16_05_2022
#define UTILS_STACK_DFS_16_05_2022

#include <set>
#include <stack>
#include <vector>

/**
 * @brief нерекурсивный дфс на стеке, изменяет visited на месте
 *
 * @param adj список смежности
 * @param root вершина, от которой строим ДФС
 * @param visited массив bool, где храним метки посещена/не посещена вершина
 * @return ** void
 */
void stackDFS(std::vector<std::set<int>> *adj, int root, std::vector<bool> *visited);

#endif
