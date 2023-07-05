from zad5ktesty import runtests


def garek(A):
    # Tutaj proszę wpisać własną implementację
    n = len(A)
    F = [[(0, 0) for _ in range(n)] for _ in range(n)]
    res = 0
    F[n-1][n-1] = (A[n-1], 0)
    for i in range(n-1):
        F[i][i] = (A[i], 0)
        F[i][i+1] = (max(A[i], A[i+1]), min(A[i], A[i+1]))

    def f(A, F, i, j):
        if F[i][j] != (0, 0):
            return F[i][j]
        if A[i]+f(A, F, i+1, j)[1] > A[j]+f(A, F, i, j-1)[1]:
            F[i][j] = (A[i]+F[i+1][j][1], f(A, F, i+1, j)[0])
        else:
            F[i][j] = (A[j]+F[i][j-1][1], f(A, F, i, j-1)[0])
        return F[i][j]

    f(A, F, 0, n-1)

    return F[0][n-1][0]


T = [8, 15, 3, 7]


# def check(A):
#     F = garek(A)
#     for i in F:
#         print(i)


# check(T)

runtests(garek)
