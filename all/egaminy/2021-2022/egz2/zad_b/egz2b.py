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
                    # print(i, F[i], j)
    # print(F)

    return F[n-1]


C = [[2, [5, 1], [1, 6], [1, 8]],
     [2, [7, 2], [1, 4], [1, 2]],
     [89, [91, 3], [75, 8], [84, 6]],
     [8, [6, 4], [10, 6], [7, 5]],
     [4, [5, 5], [1, 7], [3, 5]],
     [10, [11, 6], [0, 6], [4, 6]],
     [1, [0, 7], [0, 7], [6, 7]],
     [57, [51, 8], [45, 8], [50, 8]],
     [2, [6, 9], [7, 9], [0, 9]],
     [6, [3, -1], [8, -1], [1, -1]]]

magic(C)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
