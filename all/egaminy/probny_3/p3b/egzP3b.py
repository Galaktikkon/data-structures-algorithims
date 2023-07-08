from egzP3btesty import runtests
from queue import PriorityQueue

G = [
    [(1, 15), (2, 5), (3, 10)],
    [(0, 15), (2, 8), (4, 5), (5, 12)],
    [(0, 5), (1, 8), (3, 5), (4, 6)],
    [(0, 10), (2, 5), (4, 2), (5, 11)],
    [(1, 5), (2, 6), (3, 2), (5, 2)],
    [(1, 12), (4, 2), (3, 11)]
]


def get_edges(G):
    E = []
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                E.append([i, G[i][j][0], G[i][j][1]])
    return E


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findSet(x):
    if x.parent != x:
        x.parent = findSet(x.parent)
    return x.parent


def findUnion(x, y):
    x = findSet(x)
    y = findSet(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal(E, n):
    V = [Node(i) for i in range(n)]
    E.sort(key=lambda x: x[2], reverse=1)
    cost = 0
    max_last = 0
    for e in E:
        u, v, w = e
        if findSet(V[u]) != findSet(V[v]):
            findUnion(V[u], V[v])
            cost += w
        else:
            max_last = max(w, max_last)
    return cost+max_last


def get_sum(G):
    n = len(G)
    result = 0
    for i in range(n):
        for j in range(len(G[i])):
            result += G[i][j][1]
    return result//2


def lufthansa(G):
    # tutaj proszę wpisać własną implementację
    E = get_edges(G)
    n = len(G)
    return get_sum(G)-Kruskal(E, n)


runtests(lufthansa, all_tests=True)
