#  mając tablice skoków A, obliczyć na ile sposobów można się dostać na pole n-1, skacząc o maksymalnie wartość A[i]


def rec_stairs(A):
    n = len(A)
    F = [0 for _ in range(n)]
    F[0] = 1
    for i in range(n):
        j = 1
        while i+j < n and j <= A[i]:
            F[i+j] += F[i]
            j += 1
    return F


A = [1, 3, 2, 1, 0]
print(rec_stairs(A))
