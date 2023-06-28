# Given a gold mine called M of (n x m) dimensions.
# Each field in this mine contains a positive integer which is the amount of gold in tons.
# Initially the miner can start from any row in the first column.
# From a given cell, the miner can move:

#     to the cell diagonally up towards the right
#     to the right
#     to the cell diagonally down towards the right

# Find out maximum amount of gold which he can collect.

def maxGold(n, m, M):
    from math import inf
    res = -inf
    F = [[0 for _ in range(m)] for _ in range(n)]
    # edge cases
    if m == 1:
        for i in range(n):
            res = max(res, M[i][0])
        return res
    if n == 1:
        return max(M[0])
    # beg conds
    for i in range(n):
        F[i][0] = M[i][0]
    # fun realisation
    for j in range(m):
        for i in range(n):
            if i == 0:
                F[i][j] = max(F[i][j-1], F[i+1][j-1])+M[i][j]
            elif i == n-1:
                F[i][j] = max(F[i][j-1], F[i-1][j-1])+M[i][j]
            else:
                F[i][j] = max(F[i][j-1], F[i+1][j-1], F[i-1][j-1])+M[i][j]
            if j == m-1:
                res = max(res, F[i][j])
    return res


M = [[1, 3, 3],
     [2, 1, 4],
     [0, 6, 4]]

n = 3
m = 3

n = 4
m = 4
M = [[1, 3, 1, 5],
     [2, 2, 4, 1],
     [5, 0, 2, 3],
     [0, 6, 1, 2]]

n = 2
m = 1
M = [[1],
     [2]]


# def check(n, m, M):
#     F = maxGold(n, m, M)
#     for i in F[0]:
#         print(i)
#     print("maximum amount of gold is: ", F[1])


# check(n, m, M)
print(maxGold(n, m, M))
