from zad4ktesty import runtests


def falisz(T):
    # Tutaj proszę wpisać własną implementację
    n = len(T)
    F = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        F[0][i] = F[0][i-1]+T[0][i]
        F[i][0] = F[i-1][0]+T[i][0]
    for i in range(1, n):
        for j in range(1, n):
            F[i][j] = min(F[i-1][j], F[i][j-1])+T[i][j]
    return F[n-1][n-1]


# def falisz(T):
#     from math import inf
#     n = len(T)
#     F = [[inf for _ in range(n)] for _ in range(n)]
#     F[0][0] = 0
#     for i in range(1, n):
#         F[0][i] = F[0][i-1]+T[0][i]
#         F[i][0] = F[i-1][0]+T[i][0]

#     def rec_fun(F, T, i, j):
#         if i < 0 or j < 0:
#             return inf
#         if F[i][j] != inf:
#             return F[i][j]

#         res = min(rec_fun(F, T, i-1, j), rec_fun(F, T, i, j-1)) + T[i][j]
#         if res != inf:
#             F[i][j] = res
#         return res

#     return rec_fun(F, T, n-1, n-1)


runtests(falisz)
