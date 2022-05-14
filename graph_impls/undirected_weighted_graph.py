class UndirectedWeightedGraph:
    def __init__(self, v):
        self.adj = {k: [] for k in range(1, v + 1)}
        self.v = v
        self.e = 0

    def add_edge(self, a, b, w):
        if a not in self.adj:
            self.add_node(a)
        if b not in self.adj:
            self.add_node(b)
        adj_a = [n for n, w in self.adj[a]]
        adj_b = [n for n, w in self.adj[b]]
        if b not in adj_a and a not in adj_b:
            if a != b:
                self.adj[a].append((b, w))
            self.adj[b].append((a, w))
            self.e += 1

    def remove_edge(self, a, b):
        ne1 = self.adj[a]
        ne2 = self.adj[b]
        if ne1 is None or ne2 is None:
            return
        for n, w in ne1:
            if n == b:
                ne1.remove((n, w))
                break
        for n, w in ne2:
            if n == a:
                ne2.remove((n, w))
                break
        self.e -= 1

    def add_node(self, a):
        if a not in self.adj:
            self.adj[a] = []
            self.v += 1

    def remove_node(self, a):
        ne1 = self.adj[a]
        self.e -= len(ne1)
        for n, w in ne1:
            self.adj[n].remove((a, w))
        self.adj.pop(a)
        self.v -= 1

    def has_node(self, key):
        return key in self.adj.keys()

    def has_edge(self, a, b):
        ne1 = []
        ne2 = []
        if a in self.adj:
            ne1 = [n for n, w in self.adj[a]]
        if b in self.adj:
            ne2 = [n for n, w in self.adj[b]]
        return b in ne1 and a in ne2

    def node_neighbours_with_weights(self, a):
        return self.adj[a]

    def node_neighbours(self, a):
        return [n for n, w in self.adj[a]]

    def __str__(self):
        result = ""
        for k, v in self.adj.items():
            result += str(k) + " - " + str(v) + "\n"
        return result
