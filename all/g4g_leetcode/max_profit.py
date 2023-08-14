def maxProfit(prices):
    from math import inf
    n = len(prices)
    F = [[-inf for _ in range(3)] for _ in range(n+1)]
    F[0][1] = 0
    for i in range(1, n+1):

        F[i][2] = F[i-1][0]+prices[i-1]
        F[i][0] = max(F[i-1][0], F[i-1][1]-prices[i-1])
        F[i][1] = max(F[i-1][1], F[i-1][2])

    return max(F[n][0], F[n][1], F[n][2])


prices = [4, 3, 2, 10, 11, 0, 11]

maxProfit(prices)
