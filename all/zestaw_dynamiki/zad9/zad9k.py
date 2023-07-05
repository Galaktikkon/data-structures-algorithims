from zad9ktesty import runtests


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


T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10


def check(T, l1, l2):
    res = prom(T, l1, l2)
    # for i in range(len(res[1])):
    #     print(i)
    #     for j in res[1][i]:
    #         print(j)
    # print(res[0])


# check(T, l1, l2)

runtests(prom)
