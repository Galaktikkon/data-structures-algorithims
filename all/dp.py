from math import inf
import bisect

# KNAPSACK


def knapsack(W, P, B):
    n = len(W)
    F = [[0 for _ in range(B+1)] for _ in range(n)]
    parent = [[False for _ in range(B+1)] for _ in range(n)]
    I = []
    for b in range(W[0], B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b-W[i] >= 0:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]]+P[i])
                parent[i][b] = True
    i = n-1
    j = B
    while j >= 0 and i >= 0:
        if parent[i][j]:
            I.append(i)
            j -= W[i]
            i -= 1
        else:
            i -= 1

    return F[n-1][B], I

# N^2 LIS


def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j]+1 > F[i]:
                P[i] = j
                F[i] = F[j]+1

    return F, P

# PROM


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

    count = rec_prom(F, P, g, d, 0)
    i, a, b = 0, g, d
    board_g = []
    board_d = []
    flag = -1
    while i < len(P) and (a >= P[i] or P[i] <= b):

        if a < P[i]:
            p1 = 0
            p2 = 1
        elif b < P[i]:
            p1 = 1
            p2 = 0
        else:
            p1 = rec_prom(F, P, a-P[i], b, i+1)
            p2 = rec_prom(F, P, a, b-P[i], i+1)

        if p1 > p2:
            if i == count-1:
                flag = 0
            board_g += [i]
            a -= P[i]
        else:
            if i == count-1:
                flag = 1
            board_d += [i]
            b -= P[i]
        i += 1
    if flag:
        return board_d
    else:
        return board_g

# AUTOSTRADA


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
            for p in range(i, j):
                res = min(res, max(f(T, F, i, p, 1), f(T, F, p+1, j, k-1)))
            F[i][j][k] = res

            return F[i][j][k]

    f(T, F, 0, n-1, k)

    return F[0][n-1][k]

# DYWANY


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

# NLOG


def mosty(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    T.sort(key=lambda x: x[0])
    S = [T[0][1]]
    for i in range(1, n):
        if T[i][1] >= S[-1]:
            S.append(T[i][1])
        else:
            S[bisect.bisect_left(S, T[i][1])] = T[i][1]
        # print(S)

    return len(S)
