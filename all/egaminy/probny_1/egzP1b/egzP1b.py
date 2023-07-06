from egzP1btesty import runtests
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


def turysta(G, D, L):
    # tutaj proszę wpisać własną implementację
    A = get_graph(G)
    n = len(A)
    T_d = [0 for _ in range(n)]
    T_l = [0 for _ in range(n)]

    for v in A[D]:
        for u, c in A[v[0]]:
            T_d[u] = c+v[1]
    for v in A[L]:
        for u, c in A[v[0]]:
            T_l[u] = c+v[1]
    path_weight = inf
    for i in range(1, n-1):
        if T_d[i] != 0 and T_l[i] != 0:
            path_weight = min(path_weight, T_d[i]+T_l[i])

    return path_weight


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

turysta(G, D, L)

runtests(turysta)
