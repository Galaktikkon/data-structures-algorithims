def dijkstra_matrix(G, s,):
    from math import inf
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    Q = [(s, 0)]
    for j in range(n):
        w = inf
        u = None
        for i in range(len(Q)):
            if Q[i][1] == d[Q[i][0]] and Q[i][1] < w:
                w = Q[i][1]
                u = Q[i][0]

        if u is None:
            break

        Q.remove((u, w))

        for v in range(n):
            if G[u][v] != -1 and d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u
                Q.append((v, d[v]))

    return parent, d


G1 = [
    [-1, 3, -1, -1, -1, -1, 2, -1, -1],
    [3, -1, 2, -1, -1, -1, -1, -1, 1],
    [-1, 2, -1, 5, -1, -1, -1, -1, -1],
    [-1, -1, 5, -1, 20, -1, -1, -1, 1],
    [-1, -1, -1, 20, -1, 8, -1, 2, -1],
    [-1, -1, -1, -1, 8, -1, 3, 1, -1],
    [2, -1, -1, -1, -1, 3, -1, 1, -1],
    [-1, -1, -1, -1, 2, 1, 1, -1, 7],
    [-1, 1, -1, 1, -1, -1, -1, 7, -1]
]

print(dijkstra_matrix(G1, 0))
