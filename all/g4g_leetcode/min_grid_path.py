def minPathCost(grid, moveCost):
    from math import inf

    m = len(grid)
    n = len(grid[0])
    F = [[inf for _ in range(n)] for _ in range(m)]

    for j in range(n):
        F[0][j] = grid[0][j]

    for i in range(1, m):
        for j in range(n):
            for k in range(n):
                F[i][j] = min(F[i][j], moveCost[grid[i-1][k]]
                              [j]+grid[i][j]+F[i-1][k])

    for i in F:
        print(i)

    sol = inf

    for j in range(n):
        sol = min(sol, F[m-1][j])

    return sol


grid = [[5, 3], [4, 0], [2, 1]]
moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]

# grid = [[5, 1, 2], [4, 0, 3]]
# moveCost = [[12, 10, 15], [20, 23, 8], [
#     21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]


minPathCost(grid, moveCost)

# TC = O(n^2*m)

# Dijkstra alternative - O(n^2*mlog(n*m))
