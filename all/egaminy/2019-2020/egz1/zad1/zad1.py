from math import inf
from zad1testy import runtests


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
            if G[vert][v] == 0 or visited[v] == True or parent[vert] == G[vert][v]:
                continue
            if d[vert] + G[vert][v] < d[v]:
                d[v] = d[vert] + G[vert][v]
                parent[v] = G[vert][v]
    return d


def islands(G, a, b):
    d = dijkstra_matrix(G, a)
    return d[b]


runtests(islands)
