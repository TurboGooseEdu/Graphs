from astro.read_astro_dataset import read_astro_dataset
from time import time


def dfs(adj: dict, root):
    # нерекурсивный ДФС
    # потом надо вынести отдельно и мб преобразовать, добавив всякие там время выхода, входа

    explored, stack = {root}, [root]

    while stack:
        u = stack.pop()
        explored.add(u)
        for v in reversed(adj[u]):
            if v not in explored:
                stack.append(v)
    return explored


def getConnectedComponents(adj):
    connected_components = 0
    visited = {key: False for key in adj.keys()}

    for i in adj.keys():
        if not visited[i]:
            explored = dfs(adj, i)
            for v in explored:
                visited[v] = True
            connected_components += 1
    return connected_components


t = time()

graph = read_astro_dataset("./pluss/CA-AstroPh.txt")
# graph = read_astro_dataset("./pluss/text.txt")

print("Время делания графа: ", time() - t)
t = time()

cc = getConnectedComponents(graph.adj)


print("Время подсчёта компонент: ", time() - t)
print("Количество компонент (290): ", cc)
