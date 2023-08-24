from zad3testy import runtests
from math import inf


def extend_graph(G):
    n = len(G)
    A = [[0 for _ in range(2*n)] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = G[i][j]

    for i in A:
        print(i)


def dijkstra_matrix(G, s):
    n = len(G)
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0

    while True:
        weight = inf
        vert = -1
        for u in range(n):
            if not visited[u] and d[u] < weight:
                weight = d[u]
                vert = u
        if vert < 0:
            break
        visited[vert] = True
        for v in range(n):
            if G[vert][v] == 0 or visited[v] == True:
                continue
            if d[vert] + G[vert][v] < d[v]:
                d[v] = d[vert] + G[vert][v]
                parent[v] = vert

    return d


G = [[0, 1, 3, 0],
     [1, 0, 1, 2],
     [3, 1, 0, 4],
     [0, 2, 4, 0]]

# print(dijkstra_matrix(G, 0))

extend_graph(G)


def jumper(G, s, w):
    pass


# runtests(jumper)
