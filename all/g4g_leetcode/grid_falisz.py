def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    F = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, n):
        F[0][i] = F[0][i-1]+grid[0][i]
    for i in range(1, m):
        F[i][0] = F[i-1][0]+grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            F[i][j] = min(F[i-1][j], F[i][j-1])+grid[i][j]
    for i in grid:
        print(i)
    print()
    for i in F:
        print(i)
    return F[m-1][n-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

minPathSum(grid)
