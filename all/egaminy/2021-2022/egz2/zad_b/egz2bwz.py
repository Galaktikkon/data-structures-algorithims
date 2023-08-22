from egz2btesty import runtests


def magic(C):
    # tu prosze wpisac wlasna implementacje
    n = len(C)
    F = [-1 for _ in range(n)]

    F[0] = 0

    for i in range(n):
        for g in range(1, 4):
            c = C[i][g][1]
            if c != -1 and F[i] != -1:
                if C[i][0] >= C[i][g][0] and C[i][0]-C[i][g][0] <= 10:
                    F[c] = max(F[c], F[i]+C[i][0]-C[i][g][0])  # type: ignore
                elif C[i][0] < C[i][g][0] and C[i][g][0]-C[i][0] <= F[i]:
                    F[c] = max(F[c], F[i]-C[i][g][0]+C[i][0])  # type: ignore

    return F[n-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
