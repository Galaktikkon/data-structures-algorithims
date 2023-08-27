from zad2testy import runtests


class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.i = None

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def nameTree(T):
    i = 0

    def dfs(root):
        nonlocal i
        root.i = i
        i += 1
        for node in root.edges:
            dfs(node)

    dfs(T)
    return i


def balance(T):
    from math import inf
    n = nameTree(T)
    F = [-1 for _ in range(n)]

    def f(F, root):

        if F[root.i] != -1:
            return F[root.i]

        edge_sum = 0
        for i, node in enumerate(root.edges):
            edge_sum += f(F, node)+root.weights[i]

        F[root.i] = edge_sum

        return F[root.i]

    f(F, T)

    sol = inf
    idx = -1
    tree_sum = max(F)

    def best_edge(F, root):
        nonlocal sol, idx, tree_sum
        for i, node in enumerate(root.edges):
            root_sum = tree_sum-root.weights[i]-F[node.i]
            node_sum = F[node.i]
            if sol > abs(root_sum-node_sum):
                sol = abs(root_sum-node_sum)
                idx = root.ids[i]
            best_edge(F, node)

    best_edge(F, T)

    return idx


runtests(balance)
