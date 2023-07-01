from zad1testy import runtests


def dijkstra_matrix(G, P, s, t, f):
    from math import inf
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    gas_stations = [False for _ in range(n)]
    for i in P:
        gas_stations[i] = True
    F = [0 for _ in range(n)]
    F[s] = f
    Q = [(s, 0, f)]
    while Q:
        print(Q)
        # print(Q)
        # print(parent)
        w = inf
        fuel = -inf
        u = None
        for i in range(len(Q)):
            if Q[i][0] != -1 and Q[i][1] < w:
                if Q[i][2] > fuel:
                    w = Q[i][1]
                    fuel = Q[i][2]
                    u = Q[i][0]
        # print(u, w, fuel, "-pop")
        Q.remove((u, w, fuel))  # type: ignore

        for v in range(n):
            if G[u][v] != -1 and G[u][v] <= fuel:
                if d[v] > d[u] + G[u][v] or F[u] - G[u][v] > F[v]:
                    d[v] = d[u] + G[u][v]
                    parent[v] = u

                    if gas_stations[v]:
                        Q.append((v, d[v], fuel))
                        F[v] = fuel
                    else:
                        Q.append((v, d[v], fuel-G[u][v]))
                        F[v] = fuel-G[u][v]
        if u == t:
            break

    return parent, d


def jak_dojade(G, P, d, a, b):
    # tu prosze wpisac wlasna implementacje
    parent, dist = dijkstra_matrix(G, P, a, b, d)
    if parent[b] is None:
        return None
    path = []
    while parent[b] != None:
        path.append(b)
        b = parent[b]
    path.append(a)
    return path[::-1]


P = [3]


# def matrix(E, n):
#     G = [[-1 for _ in range(n)] for _ in range(n)]
#     for u, v, c in E:
#         G[u][v] = G[v][u] = c
#     return G


# E = [(0, 1, 2), (1, 2, 5), (1, 4, 4), (1, 3, 7),
#      (2, 3, 1), (2, 5, 1), (4, 5, 8)]
# G = matrix(E, 6)

G2 = [
    [-1, 2, -1, -1, -1],
    [-1, -1, 1, -1, 3],
    [-1, -1, -1, 1, -1],
    [-1, 1, -1, -1, -1],
    [-1, -1, -1, -1, -1]
]

print(jak_dojade(G2, P, 10, 0, 4))

runtests(jak_dojade)
