from zad1ktesty import runtests


def roznica(S):
    # Tutaj proszę wpisać własną implementację
    n = len(S)
    F = [[0 for _ in range(n)] for _ in range(n)]
    res = -1
    for i in range(1, n):
        if S[i] == '1':
            F[0][i] = F[0][i]-1
        if S[i] == '0':
            F[0][i] = F[0][i]+1

    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                if S[j] == '1':
                    F[i][j] = -1
                if S[j] == '0':
                    F[i][j] = 1
            else:
                if S[j] == '1':
                    F[i][j] = F[i][j-1]-1
                if S[j] == '0':
                    F[i][j] = F[i][j-1]+1
            res = max(res, F[i][j])
    return res


S = '11000010001'


# def check(S):
#     F = roznica(S)
#     for i in F:
#         print(i)


# check(S)

runtests(roznica)
