import sys
sys.setrecursionlimit(10**6)


def knightDialer(n):
    mod = (10**9)+7
    F = [[-1 for _ in range(10)] for _ in range(n+1)]
    J = [
        [4, 6],
        [6, 8],
        [7, 9],
        [4, 8],
        [0, 3, 9],
        [],
        [0, 1, 7],
        [2, 6],
        [1, 3],
        [2, 4]
    ]
    for i in range(10):
        F[1][i] = 1

    def f(J, F, pos, moves, mod):

        if moves == 0:
            return 0

        if F[moves][pos] != -1:
            return F[moves][pos] % mod
        s = 0
        for i in J[pos]:
            s += f(J, F, i, moves-1, mod) % mod
        F[moves][pos] = s % mod
        return F[moves][pos] % mod
    sol = 0
    for i in range(10):
        sol += f(J, F, i, n, mod)
    return sol % mod


n = 3131

knightDialer(n)
