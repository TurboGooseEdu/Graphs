class DirectedGraph:
    def __init__(self, name="Untitled directed graph"):
        self.name = name
        self.adj = {}
        self.v = 0
        self.e = 0

    def add_edge(self, a, b):
        self.add_node(a)
        self.add_node(b)
        if b not in self.adj[a]:
            self.adj[a].add(b)
            self.e += 1

    def remove_edge(self, a, b):
        ne = self.adj[a]
        if ne is None:
            return
        if b in ne:
            self.adj[a].remove(b)
            self.e -= 1

    def add_node(self, a):
        if a not in self.adj.keys():
            self.adj[a] = set()
            self.v += 1

    def remove_node(self, a):
        self.e -= len(self.adj[a])
        for k, v in self.adj.items():
            if a in v:
                self.adj[k].remove(a)
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
        n = set()
        for k, v in self.adj.items():
            if a in v:
                n.add(k)
        return n

    def __str__(self):
        result = ""
        for k, v in self.adj.items():
            result += str(k) + " - " + str(v) + "\n"
        result += "V: {}, E: {}\n".format(self.v, self.e)
        return result
