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