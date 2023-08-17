def minFallingPathSum(matrix):
    from math import inf
    n = len(matrix)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        F[0][j] = matrix[0][j]
    sol = inf
    for i in range(1, n):
        for j in range(n):
            if j == 0:
                F[i][j] = min(F[i-1][j], F[i-1][j+1])+matrix[i][j]
            elif j == n-1:
                F[i][j] = min(F[i-1][j], F[i-1][j-1])+matrix[i][j]
            else:
                F[i][j] = min(F[i-1][j+1], F[i-1][j], F[i-1][j-1])+matrix[i][j]

    for j in range(n):
        sol = min(sol, F[n-1][j])

    return sol


matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]

matrix = [[-19, 57], [-40, -5]]

minFallingPathSum(matrix)
