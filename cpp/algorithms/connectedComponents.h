#ifndef ALGORITHMS_CONNECTED_COMPONENTS_16_05_2022
#define ALGORITHMS_CONNECTED_COMPONENTS_16_05_2022

#include "../graphs/UndirectedGraph.h"
#include "../utils/dfs.h"
#include "../utils/stack_dfs.h"
#include <vector>

/**
 * @brief Function that perfoms depth first search algorithm on graph
 * and calculated the number of connected components.
 *
 * @param adj adjacency list of graph.
 *
 * @return connected_components number of connected components in graph.
 */
int getConnectedComponents(UndirectedGraph g);

#endif
