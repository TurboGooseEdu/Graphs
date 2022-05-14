class DirectedGraph:
    def __init__(self, v):
        self.adj = {k: [] for k in range(1, v + 1)}
        self.v = v
        self.e = 0

    def add_edge(self, a, b):
        if a not in self.adj.keys():
            self.add_node(a)
        if b not in self.adj.keys():
            self.add_node(b)
        if b not in self.adj[a]:
            self.adj[a].append(b)
            self.e += 1

    def remove_edge(self, a, b):
        ne1 = self.adj[a]
        ne2 = self.adj[b]
        if ne1 is None or ne2 is None:
            return
        ne1.remove(b)
        self.e -= 1

    def add_node(self, a):
        if a not in self.adj:
            self.adj[a] = []
            self.v += 1

    def remove_node(self, a):
        self.e -= len(self.adj[a])
        for k, v in self.adj.items():
            if a in v:
                v.remove(a)
                self.e -= 1
        self.adj.pop(a)
        self.v -= 1

    def has_node(self, key):
        return key in self.adj.keys()

    def has_edge(self, a, b):
        ne1 = []
        if a in self.adj:
            ne1 = self.adj[a]
        return b in ne1

    def outcoming_neighbours(self, a):
        return self.adj[a]

    def incoming_neighbours(self, a):
        n = []
        for k, v in self.adj.items():
            if a in v:
                n.append(k)
        return n

    def __str__(self):
        result = ""
        for k, v in self.adj.items():
            result += str(k) + " - " + str(v) + "\n"
        return result
