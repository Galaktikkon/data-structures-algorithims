from zad11ktesty import runtests
from math import inf


def prefix_sum(T):
    n = len(T)
    F = [0 for _ in range(n)]
    F[0] = T[0]
    for i in range(1, n):
        F[i] = F[i-1]+T[i]
    return F


def kontenerowiec(T):
    # Tutaj proszę wpisać własną implementację
    n = len(T)
    p = sum(T)
    F = [[-1 for _ in range(p+1)] for _ in range(n)]
    L = prefix_sum(T)

    def f(F, T, L, p, i):

        if i == len(T)-1:
            return abs((L[i]-p)-p)

        if F[i][p] != -1:
            return F[i][p]
        F[i][p] = min(f(F, T, L, p+T[i], i+1), f(F, T, L, p, i+1))

        return F[i][p]

    f(F, T, L, 0, 0)

    return F[0][0]


runtests(kontenerowiec)
