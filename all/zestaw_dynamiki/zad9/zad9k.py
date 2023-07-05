from zad9ktesty import runtests
from math import inf


def prom(P, g, d):
    n = len(P)
    F = [[[-1 for _ in range(d+1)] for _ in range(g+1)] for _ in range(n)]

    def rec_prom(F, P, g, d, i):
        if i == len(P):
            return 0

        if g < P[i] and d < P[i]:
            F[i][g][d] = 0
            return 0

        if F[i][g][d] != -1:
            return F[i][g][d]
        if P[i] > g:
            F[i][g][d] = rec_prom(F, P, g, d-P[i], i+1)+1
        elif P[i] > d:
            F[i][g][d] = rec_prom(F, P, g-P[i], d, i+1)+1
        else:
            F[i][g][d] = max(rec_prom(F, P, g-P[i], d, i+1),
                             rec_prom(F, P, g, d-P[i], i+1))+1

        return F[i][g][d]

    rec_prom(F, P, g, d, 0)

    return F


T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10


def check(T, l1, l2):
    F = prom(T, l1, l2)
    for i in range(len(F)):
        print(i)
        for j in F[i]:
            print(j)


check(T, l1, l2)

# runtests(prom)
