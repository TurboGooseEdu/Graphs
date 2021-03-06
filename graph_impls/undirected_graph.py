class UndirectedGraph:
    def __init__(self, name="Untitled undirected graph"):
        self.name = name
        self.adj = {}
        self.v = 0
        self.e = 0

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        if b not in self.adj[a] and a not in self.adj[b]:
            self.adj[a].add(b)
            self.adj[b].add(a)
            self.e += 1

    def remove_edge(self, a, b):
        ne1 = self.adj[a]
        ne2 = self.adj[b]
        if ne1 is None or ne2 is None:
            return
        if b in ne1 or a in ne2:
            ne1.remove(b)
            ne2.remove(a)
            self.e -= 1

    def add_node(self, a):
        if a not in self.adj.keys():
            self.adj[a] = set()
            self.v += 1

    def remove_node(self, a):
        ne1 = self.adj[a]
        self.e -= len(ne1)
        for node in ne1.copy():
            self.adj[node].remove(a)
        self.adj.pop(a)
        self.v -= 1

    def has_node(self, key):
        return key in self.adj.keys()

    def has_edge(self, a, b):
        ne1 = []
        ne2 = []
        if a in self.adj:
            ne1 = self.adj[a]
        if b in self.adj:
            ne2 = self.adj[b]
        return b in ne1 and a in ne2

    def node_neighbours(self, a):
        return self.adj[a]

    def __str__(self):
        result = ""
        for k, v in self.adj.items():
            result += str(k) + " - " + (str(v) if v else "{}") + "\n"
        result += "V: {}, E: {}\n".format(self.v, self.e)
        return result
