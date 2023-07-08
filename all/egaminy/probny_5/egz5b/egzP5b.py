from egzP5btesty import runtests


def get_graph(E):
    n = 0
    for i in range(len(E)):
        n = max(n, E[i][0], E[i][1])
    G = [[] for _ in range(n+1)]
    for u, v in E:
        G[u].append(v)
        G[v].append(u)
    return G


def clear(B):
    n = len(B)
    for i in range(n):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1], B[i][0])
    B.sort(key=lambda x: (x[0], x[1]))
    E = [B[0]]
    ptr = B[0]
    i = 1
    while i < n:
        if B[i] != ptr:
            ptr = B[i]
            E.append(ptr)
        i += 1
    return E


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


def koleje(B):
    # tutaj proszę wpisać własną implementację
    E = clear(B)
    G = get_graph(E)
    A = artics(G)

    return sum(A)


runtests(koleje, all_tests=True)
