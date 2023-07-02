from zad3ktesty import runtests


def ksuma(T, k):
    # Tutaj proszę wpisać własną implementację
    from math import inf
    n = len(T)
    F = [inf for _ in range(n)]
    res = inf
    for i in range(k):
        F[i] = T[i]
    for i in range(k, n):
        for j in range(i-k, i):
            F[i] = min(F[i], T[i]+F[j])
    for i in range(n-k, n):
        res = min(res, F[i])
    return res


T = [1, 2, 3, 4, 6, 15, 8, 7]
k = 4


def check(T, k):
    F = ksuma(T, k)
    print(F)


# check(T, k)


runtests(ksuma)
