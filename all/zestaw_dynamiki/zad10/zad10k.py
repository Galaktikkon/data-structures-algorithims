from zad10ktesty import runtests
from math import isqrt
from math import inf


def dywany(N):
    # Tutaj proszę wpisać własną implementację
    F = [-1 for _ in range(N+1)]
    F[0] = 0
    F[1] = 1

    def rec_dyw(F, N):
        res = inf

        if N < 0:
            return inf

        if F[N] != -1:
            return F[N]

        if pow(isqrt(N), 2) == N:
            F[N] = 1
            return F[N]
        else:
            for i in range(1, isqrt(N)+1):
                res = min(res, rec_dyw(F, N-pow(i, 2))+1)
            if res != inf:
                F[N] = res

        return F[N]

    rec_dyw(F, N)
    l = N
    out = []
    while l > 0:
        min_i = N
        min_l = 1
        for i in range(1, isqrt(N)+1):
            if min_i > rec_dyw(F, l-pow(i, 2)):
                min_i = rec_dyw(F, l-pow(i, 2))
                min_l = i
        out.append(min_l)
        l -= pow(min_l, 2)

    return out


runtests(dywany)
