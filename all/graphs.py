from math import inf
from queue import PriorityQueue

# TURYSTA


def relax_tourist(T, v, u, c, e):
    if T[e+1][v] > T[e][u]+c:
        T[e+1][v] = T[e][u]+c
        return True
    return False


def turysta(G, D, L):
    # tutaj proszę wpisać własną implementację
    # A = get_graph(G)
    A = []
    n = len(G)
    T = [[inf for _ in range(n)] for _ in range(5)]
    Q = PriorityQueue()
    T[0][D] = 0
    Q.put((T[0][D], 0, D))

    while not Q.empty():
        w, e, u = Q.get()
        if u == L and e == 4:
            return T[e][u]
        if e > 3:
            continue
        if w == T[e][u]:
            for v, c in A[u]:
                if relax_tourist(T, v, u, c, e):
                    Q.put((T[e+1][v], e+1, v))

# TOPOSORT


def topoSort(G):

    def DFSVisit(G, i):
        nonlocal visited, topoList
        visited[i] = True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(G, v)
        topoList.append(i)

    n = len(G)
    topoList = []
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            DFSVisit(G, i)

    return topoList

# SILNIE SPÓJNIE SKŁADOWE


def time(G):

    n = len(G)
    visited = [False for _ in range(n)]
    time_tab = [0 for _ in range(n)]
    t = n-1

    def dfsVisit(G, u):
        nonlocal visited, time_tab, t
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
        time_tab[t] = u
        t -= 1

    for i in range(n):
        if not visited[i]:
            dfsVisit(G, i)

    return time_tab


def reverse_edges(G):

    n = len(G)
    visited = [False for _ in range(n)]
    A = [[] for _ in range(n)]

    def dfsVisit(G, u):
        nonlocal visited, A
        visited[u] = True
        for v in G[u]:
            A[v].append(u)
            if not visited[v]:
                dfsVisit(G, v)

    for i in range(n):
        if not visited[i]:
            dfsVisit(G, i)

    return A


def strong_connected_components(G):

    n = len(G)
    A = reverse_edges(G)
    time_tab = time(G)
    visited = [False for _ in range(n)]
    out = []

    def dfsVisit(G, u):
        nonlocal visited, comp
        visited[u] = True
        for v in A[u]:
            if not visited[v]:
                dfsVisit(G, v)
        comp.append(u)

    for v in time_tab:
        if not visited[v]:
            comp = []
            dfsVisit(A, v)
            out.append(comp)

    return out


def s_graph(G):

    n = len(G)
    visited = [False for _ in range(n)]
    A = strong_connected_components(G)
    nc = len(A)
    S = [[] for _ in range(nc)]
    M = [[False for _ in range(nc)] for _ in range(nc)]

    belong = [0 for _ in range(n)]
    for i in range(nc):
        for j in range(len(A[i])):
            belong[A[i][j]] = i

    def dfsVisit(G, u):
        nonlocal visited, S, M, belong
        visited[u] = True

        for v in G[u]:
            if belong[v] != belong[u] and M[belong[u]][belong[v]] == False:
                M[belong[u]][belong[v]] = True
                S[belong[u]].append(belong[v])
            if not visited[v]:
                dfsVisit(G, v)

    for u in range(n):
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)

    return S

# MOSTY


def bridges(G):
    n = len(G)
    time_tab = [0 for _ in range(n)]
    t = 1
    low = [0 for _ in range(n)]
    bridges = []

    def dfsVisit(at, par):
        nonlocal t, low
        low[at] = time_tab[at] = t
        t += 1
        for v in G[at]:
            if not time_tab[v]:
                dfsVisit(v, at)
                low[at] = min(low[at], low[v])
            elif v != par:
                low[at] = min(time_tab[v], low[at])
        if time_tab[at] == low[at] and par >= 0:
            bridges.append((par, at))

    for i in range(n):
        if not time_tab[i]:
            dfsVisit(i, -1)

    return bridges

# PUNKTY ARTYKULACJI


def artics(G):
    n = len(G)
    time_tab = [0 for _ in range(n)]
    t = 1
    low = [0 for _ in range(n)]
    art_points = [False for _ in range(n)]

    def dfsVisit(root, at, par):
        nonlocal t, low, edge_count
        low[at] = time_tab[at] = t
        t += 1
        if par == root:
            edge_count += 1
        for v in G[at]:
            if not time_tab[v]:
                dfsVisit(root, v, at)
                low[at] = min(low[at], low[v])
                if time_tab[at] <= low[v]:
                    art_points[at] = True
            elif v != par:
                low[at] = min(time_tab[v], low[at])

    for i in range(n):
        if not time_tab[i]:
            edge_count = 0
            dfsVisit(i, i, -1)
            art_points[i] = (edge_count > 1)

    return art_points

# DIJKSTRA


def Dijkstra(G, s):
    from math import inf
    from queue import PriorityQueue
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if relax(parent, d, v, u, c):
                    Q.put((d[v], v))
    return parent, d


def relax(parent, d, v, u, c):
    if d[v] > d[u]+c:
        d[v] = d[u]+c
        parent[v] = u
        return True
    return False

# BELLMAN FORD


def BellmannFord(G, s):
    from math import inf
    n = len(G)
    d = [inf for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]

    for i in range(n):
        for u in range(n):
            for v, w in G[u]:
                relax(parent, d, v, u, w)

    for i in range(n):
        for u in range(n):
            for v, w in G[u]:
                if d[v] > d[u]+w:
                    d[v] = -inf

    return d, parent

# FLOYD WARSHALL


def floydRelax(S, x, t, y, parent):
    if x == y:
        S[x][y] = 0
    if S[x][t]+S[t][y] < S[x][y]:
        S[x][y] = S[x][t]+S[t][y]
        parent[x][y] = t
        return True

    return False


def FloydWarshall(G):
    from math import inf
    from copy import deepcopy
    n = len(G)
    S = deepcopy(G)
    P = [[None for _ in range(n)] for _ in range(n)]
    for t in range(n):
        for x in range(n):
            for y in range(n):
                floydRelax(S, x, t, y, P)

    for t in range(n):
        for x in range(n):
            for y in range(n):
                if S[x][t]+S[t][y] < S[x][y]:
                    S[x][y] = -inf
                    # P[x][y]=-inf # type: ignore

    return S, P

# KRUSKAL


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findSet(x):
    if x.parent != x:
        x.parent = findSet(x.parent)
    return x.parent


def findUnion(x, y):
    x = findSet(x)
    y = findSet(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def Kruskal(E, n):
    A = []
    V = [Node(i) for i in range(n)]
    # G=[[] for _  in range(n)]
    E.sort(key=lambda x: x[2])
    cost = 0
    for e in E:
        u, v, w = e
        if findSet(V[u]) != findSet(V[v]):
            findUnion(V[u], V[v])
            # G[u].append((v,w)) opcja dla zwrotu w postaci listy sąsiedztwa
            A += [e]
            cost += w
    return A, cost

# PRIM


def prim(G, s):
    n = len(G)
    from math import inf
    from queue import PriorityQueue
    d = [inf for _ in range(n)]
    d[s] = 0
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    Q = PriorityQueue()
    Q.put((d[s], s))
    while not Q.empty():
        w, u = Q.get()
        for v, c in G[u]:
            if not visited[v]:
                if c < d[v]:
                    d[v] = c
                    parent[v] = u
                    Q.put((d[v], v))
                    visited[u] = True
    cost = sum(d, 0)
    return parent, d, cost

# FORD FULKERSON


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
