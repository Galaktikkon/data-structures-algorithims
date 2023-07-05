from zad7ktesty import runtests


def dfs(T, D):
    n = len(T)
    m = len(T[0])
    w_len = len(D)
    W = [0 for _ in range(w_len)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs_visit(T, i, j, n, m):
        nonlocal visited, water
        if not visited[i][j]:
            visited[i][j] = True
            for u, w in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                if 0 <= u+i < n and 0 <= w+j < m:
                    if T[u+i][w+j] > 0 and not visited[i+u][j+w]:
                        dfs_visit(T, i+u, j+w, n, m)
            water += T[i][j]
    for i in range(w_len):
        water = 0
        dfs_visit(T, 0, D[i], n, m)
        W[i] = water

    return W


def ogrodnik(T, D, Z, l):
    W = dfs(T, D)
    n = len(D)
    F = [[0 for _ in range(l+1)] for _ in range(n)]

    for b in range(W[0], l+1):
        F[0][b] = Z[0]
    for b in range(l+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if W[i] <= b:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]]+Z[i])
    return F[n-1][l]


runtests(ogrodnik, all_tests=True)
