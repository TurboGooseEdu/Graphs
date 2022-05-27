#include "Graph.h"
#include <algorithm>
#include <ctime>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::map;
using std::set;
using std::vector;

// Могут быть любые отрицательные числа
const int ROOT_VALUE = -1;
const int NO_DATA_VALUE = -2;

// Алгоритм поиска аппроксимационного расстояния
enum AlgoMode {
    Basic = 0, // Базовый алгоритм
    SC = 1     // ShortCutting
};

// Алгоритм выбора опорных точек
enum LandmarkSelection {
    Random = 0,        // Случайный выбор
    HighestDegree = 1, // Вершины с наибольшей степенью
    BestCoverage = 2   // Вершины с лучшим покрытием
};

/**
 * @brief Вспомогательный метод.
 * Получить пары рандомных вершин в интервале от 0 до n-1.
 * Вершины не повторяются.
 *
 * @param n общее количество вершин графа
 * @param m число пар вершин
 * @return ** vector<std::pair<int, int>>
 */
vector<std::pair<int, int>> getRandomVertices(int n, int m) {
    if (2 * m > n)
        return vector<std::pair<int, int>>();

    vector<int> vertices = vector<int>(n);
    std::iota(vertices.begin(), vertices.end(), 0);

    int left = n;

    vector<std::pair<int, int>> randVertices = vector<std::pair<int, int>>();
    for (int i = 0; i < 2 * m; i += 2) {
        std::pair<int, int> v_pair;
        int r;

        r = std::rand() % left;
        v_pair.first = vertices[i + r];
        std::swap(vertices[i], vertices[i + r]);
        --left;

        r = std::rand() % left;
        v_pair.second = vertices[i + 1 + r];
        std::swap(vertices[i + 1], vertices[i + 1 + r]);
        --left;

        randVertices.push_back(v_pair);
    }

    return randVertices;
}
vector<int> pathTo(int s, vector<int> *path, vector<int> *SPT) {
    // путь от s до любой вершины из path, с помощью прохода по SPT
    set<int> p = set<int>(path->begin(), path->end());
    vector<int> resPath = {s};
    while (p.find(s) == p.end() && s >= 0) {
        s = (*SPT)[s];
        resPath.push_back(s);
    }
    if (s != NO_DATA_VALUE)
        return resPath;
    return vector<int>{NO_DATA_VALUE};
}

vector<int> pathTo(int s, int t, vector<int> *SPT) {

    vector<int> resPath = {s};
    while (s != t && s >= 0) {
        s = (*SPT)[s];
        resPath.push_back(s);
    }
    if (s != NO_DATA_VALUE)
        return resPath;
    return vector<int>{NO_DATA_VALUE};
}

vector<int> BFS(vector<set<int>> *adj, int s) {
    // просмотреть весь граф и вернуть длину путей

    vector<int> pathLengths = vector<int>(adj->size(), NO_DATA_VALUE);
    std::queue<int> q;

    q.push(s);
    pathLengths[s] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : (*adj)[u])
            if (pathLengths[v] == NO_DATA_VALUE) {
                pathLengths[v] = pathLengths[u] + 1;
                q.push(v);
            }
    }
    return pathLengths;
}
int BFS(vector<set<int>> *adj, int s, int t) { //? done, not checked
    // просмотреть пока не найдём вершину и вернуть длину пути

    if (s == t)
        return 0;

    vector<int> pathLengths = vector<int>(adj->size(), NO_DATA_VALUE);
    pathLengths[s] = 0;
    std::queue<int> q;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        if (u == t) {
            return pathLengths[u];
        }
        q.pop();
        for (int v : (*adj)[u])
            if (pathLengths[v] == NO_DATA_VALUE) {
                pathLengths[v] = pathLengths[u] + 1;
                q.push(v);
            }
    }
    return NO_DATA_VALUE;
};
vector<int> BFSWithPaths(vector<set<int>> *adj, int s) {
    // просмотреть весь граф и в каждую вершину записать "указатель" на родителя
    vector<int> parentOf = vector<int>(adj->size(), NO_DATA_VALUE);
    std::queue<int> q;

    q.push(s);
    parentOf[s] = ROOT_VALUE;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : (*adj)[u])
            if (parentOf[v] == NO_DATA_VALUE) {
                parentOf[v] = u;
                q.push(v);
            }
    }
    return parentOf;
}
set<int> BFSWithPaths(vector<set<int>> *adj, int s, int t) { // done, not checked
    if (s == t)
        return set<int>{s};

    vector<int> parentOf = vector<int>(adj->size(), NO_DATA_VALUE);
    set<int> path;
    std::queue<int> q;

    q.push(s);
    parentOf[s] = ROOT_VALUE;

    while (!q.empty()) {
        int u = q.front();
        if (u == t) {
            break;
        }
        q.pop();
        for (int v : (*adj)[u])
            if (parentOf[v] == NO_DATA_VALUE) {
                parentOf[v] = u;
                q.push(v);
            }
    }
    // если так и не дошли до t - пустое множество
    if (parentOf[t] == NO_DATA_VALUE)
        return set<int>();

    int parent = t;

    // цикл: пока не дойдём до корня, добавляем каждую вершину в множество
    while (parent != ROOT_VALUE) {
        path.insert(parent);
        parent = parentOf[parent];
    }
    return path;
}

int getApproximateDistance(
    vector<set<int>> *adj, int s, int t, vector<vector<int>> *distances, vector<int> *landmarks, AlgoMode mode) {
    vector<int> stDistances;
    switch (mode) {
    case Basic: {
        for (auto d : *distances)
            if (d[s] != NO_DATA_VALUE && d[t] != NO_DATA_VALUE)
                stDistances.push_back(d[s] + d[t]);
        break;
    }
    case SC: {
        int landmarkCount = 0;
        for (auto SPT : *distances) {
            vector<int> p0 = pathTo(s, (*landmarks)[landmarkCount], &SPT);
            if (p0[0] == NO_DATA_VALUE) {
                stDistances.push_back(NO_DATA_VALUE);
                landmarkCount++;
                continue;
            }
            vector<int> p2 = pathTo(t, &p0, &SPT);
            if (p2[0] == NO_DATA_VALUE) {
                stDistances.push_back(NO_DATA_VALUE);
                landmarkCount++;
                continue;
            }
            vector<int> p1 = pathTo(s, *p2.rbegin(), &SPT);
            if (p1[0] == NO_DATA_VALUE) {
                stDistances.push_back(NO_DATA_VALUE);
                landmarkCount++;
                continue;
            }
            int Best = p2.size() + p1.size();

            for (int p1_index = 0; p1_index < p1.size(); ++p1_index)
                for (int p2_index = 0; p2_index < p2.size(); ++p2_index) {
                    int w1 = p1[p1_index];
                    int w2 = p2[p2_index];
                    if ((*adj)[w1].find(w2) != (*adj)[w1].end()) {
                        int Current = p1_index + p2_index + 1;
                        Best = std::min(Current, Best);
                    }
                }
            stDistances.push_back(Best);
            landmarkCount++;
        }
        break;
    }
    }

    int min_el = __INT_MAX__;
    for (auto l : stDistances) {
        if (min_el > l && l >= 0)
            min_el = l;
    }
    return min_el;
};

void fOutActualPaths(vector<set<int>> *adj, vector<std::pair<int, int>> vertexPairs, std::string name) {
    std::ofstream out("./actualPaths-" + name + ".txt");

    if (!out.is_open())
        return;

    for (auto vertexPair : vertexPairs) {
        int s = vertexPair.first;
        int t = vertexPair.second;
        int pathLength = BFS(adj, s, t);
        if (pathLength == NO_DATA_VALUE)
            out << s << "," << t << "," << __INT_MAX__ << endl;
        else
            out << s << "," << t << "," << pathLength << endl;
    }

    out.close();
};

vector<int> selectLandmarks(vector<set<int>> *adj, int k, LandmarkSelection mode) {
    int n = adj->size();

    vector<int> landmarks;

    switch (mode) {
    case Random: {
        vector<int> vertices = vector<int>(n, 0);
        std::iota(vertices.begin(), vertices.end(), 0);

        for (int i = 0, left = n; i < k; ++i, --left) {
            int r = std::rand() % left;
            landmarks.push_back(vertices[i + r]);
            std::swap(vertices[i], vertices[i + r]);
        }
        break;
    }
    case HighestDegree: {
        vector<int> degrees = vector<int>(n);
        // 1. Считаем для каждой вершины степень
        for (int i = 0; i < n; ++i)
            degrees[i] = (*adj)[i].size();
        // 2. Создаём очередь с приоритетами из степень+индекс
        std::priority_queue<std::pair<int, int>> q;
        for (int i = 0; i < n; ++i)
            q.push(std::pair<int, int>(degrees[i], i));
        // 3. Вытаскиваем индекс максимального по степени элемента
        for (int i = 0; i < k && !q.empty(); ++i) {
            landmarks.push_back(q.top().second);
            q.pop();
        }
        break;
    }
    case BestCoverage: {
        map<int, int> P = map<int, int>();
        vector<std::pair<int, int>> vertices = getRandomVertices(n, 100);
        // 1. Для произвольно выбранных вершин сохраняем точные пути между ними
        for (auto v : vertices) {
            int s = v.first;
            int t = v.second;
            set<int> path = BFSWithPaths(adj, s, t);
            for (auto w : path)
                ++P[w];
        }

        // 2. Составляем очередь с приоритетами по количеству попаданий вершины в объединение путей
        std::priority_queue<std::pair<int, int>> q;
        for (auto m : P)
            q.push(std::pair<int, int>(m.second, m.first));

        // 3. Выбираем самые часто встречающиеся в объединении путей вершины
        for (int i = 0; i < k && !q.empty(); ++i) {
            landmarks.push_back(q.top().second);
            q.pop();
        }
        break;
    }
    }
    return landmarks;
}

vector<vector<int>> precompute(vector<set<int>> *adj, vector<int> *landmarks, AlgoMode mode) {
    vector<vector<int>> PathTrees = vector<vector<int>>(landmarks->size(), vector<int>());
    int count = 0;

    switch (mode) {
    case Basic: {
        // Сохраняем только длины путей до каждой вершины
        for (auto landmark : *landmarks)
            PathTrees[count++] = BFS(adj, landmark);
        break;
    }
    case SC: {
        // Для каждой вершины сохраняем указатель на "родителя" при соответствующем BFS
        for (auto landmark : *landmarks) {
            PathTrees[count++] = BFSWithPaths(adj, landmark);
        }
        break;
    }
    }
    return PathTrees;
};

void process(Graph *g) {
    cout << "===========================" << endl;
    cout << "\t" << g->getName() << endl;
    cout << "===========================" << endl;

    int n = g->getVertices();
    int m = 500; //количество вершин для подсчёта аппр.расстояний

    clock_t t = clock();
    vector<std::pair<int, int>> randVertices = getRandomVertices(n, m);
    fOutActualPaths(&g->adj, randVertices, g->getName());

    cout << "Время поиска точных путей между вершинами, ms: " << (clock() - t) / 1e3 << endl;

    std::ofstream out("./landmarks-" + g->getName() + ".txt");

    if (!out.is_open())
        return;

    for (int landmarkAmount : {20, 50, 100})
        for (auto landmarkSelection : {Random, HighestDegree, BestCoverage}) {
            t = clock();
            vector<int> landmarks = selectLandmarks(&g->adj, landmarkAmount, landmarkSelection);
            cout << "Время выбора опорных точек (" << landmarkAmount << " точек; метод " << landmarkSelection << "), ms: " << (clock() - t) / 1e3 << endl;

            for (auto mode : {Basic, SC}) {
                t = clock();
                vector<vector<int>> distances = precompute(&g->adj, &landmarks, mode);
                cout << "Время преподсчёта (метод " << mode << "), ms: " << (clock() - t) / 1e3 << endl;
                t = clock();
                for (auto vertices : randVertices) {
                    int s = vertices.first;
                    int t = vertices.second;
                    int approximateDistance = getApproximateDistance(&g->adj, s, t, &distances, &landmarks, mode);
                    out << landmarkAmount << "," << landmarkSelection << "," << mode << "," << s << "-" << t << "," << approximateDistance << endl;
                }
                cout << "Время поиска приближённых путей между вершинами, ms: " << (clock() - t) / 1e3 << endl;
            }
        }
    out.close();
}

int main(int argc, char **argv) {

    std::srand(std::time(nullptr));

    // Graph *astro = new Graph("./data/astro.txt", 18772);
    // process(astro);
    // delete astro;

    // Graph *google = new Graph("./data/google.txt", 875713);
    // process(google);
    // delete google;

    Graph *vk = new Graph("./data/vk.txt", 3215722);
    process(vk);
    delete vk;

    return 0;
}
