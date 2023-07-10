from egzP8btesty import runtests
from math import inf


def FloydWarshall(G):
    n = len(G)
    for t in range(n):
        for x in range(n):
            for y in range(n):
                if x == y:
                    G[x][y] = 0
                if G[x][t]+G[t][y] < G[x][y]:
                    G[x][y] = G[x][t]+G[t][y]

    for t in range(n):
        for x in range(n):
            for y in range(n):
                if G[x][t]+G[t][y] < G[x][y]:
                    G[x][y] = -inf
    return G


def get_matrix(G):
    n = len(G)
    M = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for v, c in G[i]:
            M[i][v] = c
    return M


G = [
    [(1, 3), (2, 3)],
    [(0, 3), (4, 4)],
    [(0, 3), (3, 1), (4, 4)],
    [(2, 1), (4, 2)],
    [(1, 4), (2, 4), (3, 2)]
]
P = [0, 3, 4]


def robot(G, P):
    # Tutaj proszę wpisać własną implementację
    M = get_matrix(G)
    S = FloydWarshall(M)
    n = len(P)
    result = 0
    for i in range(n-1):
        result += S[P[i]][P[i+1]]
    return result


# print(robot(G, P))

runtests(robot, all_tests=True)
