#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <ctime>
#include <map>
#include <stack>

/**
 * @namespace graph
 * @brief Graph Algorithms
 */
namespace graph
{

    /**
     * @brief нерекурсивный дфс на стеке, изменяет visited на месте
     *
     * @param adj список смежности
     * @param root вершина, от которой строим ДФС
     * @param visited массив bool, где храним метки посещена/не посещена вершина
     * @return ** void
     */
    void nonRecursiveDFS(const std::vector<std::vector<int>> *adj, int root, std::vector<bool> *visited)
    {
        (*visited)[root] = true;

        std::stack<int> s;
        s.push(root);

        while (!s.empty())
        {
            int u = s.top();

            (*visited)[u] = true;
            s.pop();

            for (auto v : (*adj)[u])
            {
                if (!(*visited)[v])
                    s.push(v);
            }
        }
    }

    /**
     * @brief Function that perfoms depth first search algorithm on graph
     * and calculated the number of connected components.
     *
     * @param adj adjacency list of graph.
     *
     * @return connected_components number of connected components in graph.
     */
    int countWeaklyConnectedComponents(const std::vector<std::vector<int>> *components)
    {
        return components->size();
    }

    std::vector<int> getMaxWeaklyConnectedComponent(const std::vector<std::vector<int>> *components)
    {
        int max_size = 0;
        std::vector<int> max_comp;
        for (const auto& comp : *components)
        {
            if (comp.size() > max_size)
            {
                max_comp = comp;
                max_size = comp.size();
            }
        }
        return max_comp;
    }

    std::vector<std::vector<int>> getWeaklyConnectedComponents(const std::vector<std::vector<int>> *adj)
    {
        int n = adj->size();
        std::vector<bool> visited(n, false);

        std::vector<std::vector<int>> components;
        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                std::vector<int> component_vertices;
                visited[i] = true;
                std::stack<int> s;
                s.push(i);
                while (!s.empty())
                {
                    int u = s.top();
                    visited[u] = true;
                    component_vertices.push_back(u);
                    s.pop();
                    for (auto v : (*adj)[u])
                    {
                        if (!visited[v])
                            s.push(v);
                    }
                    components.push_back(component_vertices);
                }
            }
        }
        return components;
    }

    // в процессе............
    std::vector<std::vector<int>> getStronglyConnectedComponents(const std::vector<std::vector<int>> *adj) // на вход подается орграф
    {
        int time = 0;
        int n = adj->size();
        std::vector<bool> visited(n, false);
        std::vector<std::vector<int>> components;
        std::vector<int> vertices;
        std::vector<int> posts;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                {
                    visited[i] = true;
                    std::stack<int> s;
                    s.push(i);

                    while (!s.empty()) {
                        int u = s.top();

                        visited[u] = true;
                        vertices.push_back(u);
                        posts.push_back(time++);
                        s.pop();

                        for (auto v: (*adj)[u]) {
                            if (!visited[v])
                                s.push(v);
                        }
                    }
                }
            }
            return components;
        }
    }
}