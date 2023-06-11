A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def reverse(A, N, D):

    for i in range(D//2):
        A[i], A[D-i-1] = A[D-i-1], A[i]

    for i in range(D, (D+N)//2):
        A[i], A[N-1-i+D] = A[N-1-i+D], A[i]

    for i in range(N//2):
        A[i], A[N-i-1] = A[N-i-1], A[i]

    return A


N = len(A)
print(reverse(A, N, 4))
