def ways(n, m):
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(m):
        F[n][i] = 1
    for i in range(n):
        F[i][m] = 1

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            F[i][j] = F[i+1][j]+F[i][j+1]

    return F[0][0] % 10000007


print(ways(200, 200))
