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
        w = inf
        fuel = -inf
        u = None
        for i in range(len(Q)):
            if Q[i][0] != -1 and Q[i][1] < w:
                if Q[i][2] > fuel:
                    w = Q[i][1]
                    fuel = Q[i][2]
                    u = Q[i][0]

        Q.remove((u, w, fuel))

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

    return parent, d


def jak_dojade(G, P, d, a, b):
    # tu prosze wpisac wlasna implementacje
    parent, dist = dijkstra_matrix(G, P, a, b, d)
    if parent[b] is None:
        return None
    path = []
    while b != a:
        path.append(b)
        b = parent[b]
    path.append(a)
    return path[::-1]


runtests(jak_dojade)
