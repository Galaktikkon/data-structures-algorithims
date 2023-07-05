from zad12ktesty import runtests
from math import inf


def autostrada(T, k):
    # Tutaj proszę wpisać własną implementację
    n = len(T)
    if k == 1:
        return sum(T)
    F = [[[-1 for _ in range(k+1)] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        pref_sum = 0
        for j in range(i, n):
            pref_sum += T[j]
            F[i][j][1] = pref_sum

    def f(T, F, i, j, k):
        res = inf
        if k <= 0:
            return -inf
        if i > j:
            return -inf
        if F[i][j][k] != -1:
            return F[i][j][k]
        if i == j:
            F[i][j][k] = T[i]
            return F[i][j][k]
        else:
            for p in range(i, j+1):
                res = min(res, max(f(T, F, i, p, 1), f(T, F, p+1, j, k-1)))
            F[i][j][k] = res

            return F[i][j][k]

    f(T, F, 0, n-1, k)

    return F[0][n-1][k]


runtests(autostrada, all_tests=True)
