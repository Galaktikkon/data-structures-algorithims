# Marek Małek, 414880

# Algorytm opiera się na wykorsztaniu metody forda fulkersona do znalezienia największego skojarzenia w grafie - rozwiązania.
# Stworzony jest graf w dwóch reprezentacjach - macierzowej i listowej (z ktorej usuwamy i dodajemy krawędzie)

from zad6testy import runtests


def create_matrix(M):
    n = len(M)
    G = [[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    for u in range(n):
        for v in M[u]:
            G[u][n+v] = 1
    for i in range(n):
        G[2*n][i] = 1
    for i in range(n):
        G[n+i][2*n+1] = 1

    return G


def create_graph(M):
    n = len(M)
    G = [[] for _ in range(2*n+2)]
    for i in range(n):
        for j in range(len(M[i])):
            G[i].append(M[i][j]+n)
    for i in range(n):
        G[2*n].append(i)
    for i in range(n):
        G[i+n].append(2*n+1)
    return G


def bfs(G, a, b, M):
    n = len(G)
    s = a
    t = b
    from collections import deque
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [None for _ in range(n)]
    path = []
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        if u == t:
            while t != None:
                path.append(t)
                t = parent[t]
            return path[::-1]
        for v in M[u]:
            if not visited[v] and G[u][v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)

    return path[::-1]


def cap(G, path):
    s = G[path[0]][path[1]]
    for i in range(1, len(path)-1):
        s = min(s, G[path[i]][path[i+1]])
    return s


def update(G, path, M):
    w = cap(G, path)
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        M[path[i]].remove(path[i+1])
        G[path[i+1]][path[i]] += w
        M[path[i+1]].append(path[i])


def FordFulkerson(G, s, t, M):
    from copy import deepcopy
    flow = 0
    path = bfs(G, s, t, M)
    while path:
        flow += cap(G, path)
        update(G, path, M)
        path = bfs(G, s, t, M)
    return flow


def binworker(M):
    # tu prosze wpisac wlasna implementacje
    n = len(M)
    G = create_matrix(M)
    F = create_graph(M)

    return FordFulkerson(G, 2*n, 2*n+1, F)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
