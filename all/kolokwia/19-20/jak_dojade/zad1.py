from zad1testy import runtests


def relax(parent, d, v, u, weight):
    if d[v] > d[u]+weight:
        d[v] = d[u]+weight
        parent[v] = u
        return True
    return False


def dijkstra_matrix(G, P, s, t, f):
    from math import inf
    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    fuel = f
    gas_stations = [False for _ in range(n)]
    for i in P:
        gas_stations[i] = True
    q = [s]
    index = 0
    while True:
        u = q[index]
        flag = False

        if gas_stations[u]:
            fuel = f

        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v] != -1 and G[u][v] <= fuel:
                if d[v] > d[u]+G[u][v]:
                    fuel -= G[u][v]
                    d[v] = d[u]+G[u][v]
                    parent[v] = u
                    q.append(v)
                    index += 1
                    flag = True
                elif G[u][v] != -1 and G[u][v] <= fuel and fuel > d[v]:
                    fuel -= G[u][v]
                    d[v] = d[u]+G[u][v]
                    parent[v] = u
                    q.append(v)
                    index += 1
                    flag = True

        if u == t:
            break

        if not flag:
            break

    return parent, d


def jak_dojade(G, P, d, a, b):
    # tu prosze wpisac wlasna implementacje
    parent, dist = dijkstra_matrix(G, P, a, b, d)
    if parent[b] is None:
        return None
    path = []
    while b != None:
        path.append(b)
        b = parent[b]
    print(path)
    return path[::-1]


runtests(jak_dojade)
