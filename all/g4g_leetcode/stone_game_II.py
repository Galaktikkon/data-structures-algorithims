# SOL 1.

def stoneGameII(piles):
    n = len(piles)
    F = [[-1 for _ in range(n)] for _ in range(n)]
    S = [0 for _ in range(n)]
    S[n-1] = piles[n-1]
    for i in range(n-2, -1, -1):
        S[i] = S[i+1]+piles[i]

    def f(F, i, m):
        nonlocal n

        if i >= n:
            return 0

        if F[i][m] != -1:
            return F[i][m]

        res = 0
        for x in range(1, (2*m)+1):
            opp_score = f(F, i+x, max(x, m))
            res = max(res, S[i]-opp_score)

        F[i][m] = res

        return F[i][m]

    f(F, 0, 1)

    return F[0][1]


piles = [2, 7, 9, 4, 4]
piles = [1, 2, 3, 4, 5, 100]
piles = [1, 1]

stoneGameII(piles)

# SOL 2


def stone_game(piles):
    from math import inf
    n = len(piles)
    F = [[[-1, -1] for _ in range(n)] for _ in range(n)]

    def f(F, i, m, p):
        nonlocal n
        if i == n:
            return 0

        if F[i][m][p] != -1:
            return F[i][m][p]

        res = 0 if p == 0 else inf
        stones = 0
        for x in range(1, (2*m)+1):
            if i+x <= n:
                stones += piles[i+x-1]
                if p == 0:
                    res = max(res, stones+f(F, i+x, max(m, x), 1))
                elif p == 1:
                    res = min(res, f(F, i+x, max(m, x), 0))
        F[i][m][p] = res

        return F[i][m][p]

    f(F, 0, 1, 0)

    for i in F:
        print(i)

    return F[0][1][0]


piles = [2, 7, 9, 4, 4]
piles = [1, 2, 3, 4, 5, 100]
piles = [1]
piles = [9, 2, 2, 8, 3, 7, 9, 9]

stone_game(piles)
