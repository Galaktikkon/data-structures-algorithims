from zad6testy import runtests


def create_graph(M):
    n = len(M)
    G = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for u in range(n):
        for v in range(len(M[u])):
            for x in range(n):
                for y in range(len(M[x])):
                    if M[u][v] == M[x][y] and u != x:
                        G[u][x] = 1
    for i in range(n):
        G[n][i] = 1
    for i in range(n):
        G[i][n+1] = 1
    return G


M = [[0, 1, 3],  # 0
     [2, 4],  # 1
     [0, 2],  # 2
     [3],  # 3
     [3, 2]]

for i in create_graph(M):
    print(i)


def bfs(G, a, b):
    n = len(G)
    s = a
    t = b
    from collections import deque
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [None for _ in range(n)]
    path = []
    Q = deque()
    Q.append(a)
    while Q:
        u = Q.popleft()
        if u == t:
            while t != None:
                path.append(t)
                t = parent[t]
            return path[::-1]
        for i in range(n):
            if not visited[i] and G[u][i]:
                visited[i] = True
                parent[i] = u
                Q.append(i)

    return path[::-1]


def cap(G, path):
    s = G[path[0]][path[1]]
    for i in range(1, len(path)-1):
        s = min(s, G[path[i]][path[i+1]])
    return s


def update(G, path):
    w = cap(G, path)
    for i in range(len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w


def FordFulkerson(G, s, t):
    from copy import deepcopy
    flow = 0
    F = deepcopy(G)
    path = bfs(F, s, t)
    while path:
        flow += cap(F, path)
        update(F, path)
        path = bfs(F, s, t)
    return flow


def binworker(M):
    # tu prosze wpisac wlasna implementacje
    G = create_graph(M)
    n = len(M)
    return FordFulkerson(G, n, n+1)


# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(binworker, all_tests=False)
