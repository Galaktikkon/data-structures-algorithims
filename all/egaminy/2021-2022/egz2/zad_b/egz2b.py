from egz2btesty import runtests


def magic(C):
    # tu prosze wpisac wlasna implementacje
    n = len(C)
    F = [-1 for _ in range(n)]

    F[0] = 0

    for i in range(1, n):
        for j in range(i):
            for g in range(1, 4):
                if C[j][g][1] == i and F[j] != -1:
                    if C[j][0] >= C[j][g][0] and C[j][0]-C[j][g][0] <= 10:
                        F[i] = max(F[i], F[j]+C[j][0]-C[j][g][0])
                    elif C[j][0] < C[j][g][0] and C[j][g][0]-C[j][0] <= F[j]:
                        F[i] = max(F[i], F[j]-C[j][g][0]+C[j][0])

    return F[n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=False)
