from egzP1btesty import runtests
from queue import PriorityQueue
from math import inf


def get_graph(E):
    n = 0
    for i in range(len(E)):
        n = max(n, E[i][0], E[i][1])
    G = [[] for _ in range(n+1)]
    for edge in E:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))
    return G


def relax(T, v, u, c, e):
    if T[e][v] > T[e][u]+c:
        T[e][v] = T[e+1][u]+c
        return True
    return False


def turysta(G, D, L):
    # tutaj proszę wpisać własną implementację
    A = get_graph(G)
    n = len(A)
    T = [[inf for _ in range(n)] for _ in range(3)]
    Q = PriorityQueue()
    T[0][D] = 0
    Q.put((T[D], -1, D))

    while not Q.empty():
        w, e, u = Q.get()
        if u == L:
            return T[e][u]
        if e > 2:
            continue
        if w == T[e][u]:
            for v, c in G[u]:
                if relax(T, v, u, c, e):
                    Q.put((T[e][v], e, v))


G = [
    (0, 1, 9), (0, 2, 1),
    (1, 2, 2), (1, 3, 8),
    (1, 4, 3), (2, 4, 7),
    (2, 5, 1), (3, 4, 7),
    (4, 5, 6), (3, 6, 8),
    (4, 6, 1), (5, 6, 1)
]
D = 0
L = 6

runtests(turysta)
