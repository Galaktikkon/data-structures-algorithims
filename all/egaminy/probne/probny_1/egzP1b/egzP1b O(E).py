from egzP1btesty import runtests
from math import inf


def get_graph(E):
    n = 0
    for i in range(len(E)):
        n = max(n, E[i][0], E[i][1])
    G = []
    for v, c, e in E:
        G.append((v, c, e))
        G.append((c, v, e))
    return G


def turysta(G, D, L):
    # tutaj proszę wpisać własną implementację
    A = get_graph(G)
    n = len(G)
    from math import inf
    F = [[inf for _ in range(5)] for _ in range(n)]

    F[D][0] = 0

    for s in range(1, 5):
        for u, v, c in A:
            if F[u][s-1] != inf:
                F[v][s] = min(F[v][s], F[u][s-1]+c)

    sol = F[L][4]

    return sol if sol != inf else -1


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
