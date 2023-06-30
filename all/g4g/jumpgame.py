def jumpgame(A, n):
    F = [False for _ in range(n)]
    P = [-1 for _ in range(n)]
    if A[0] < 1:
        return F, P
    F[0] = True
    fuel = A[0]
    p_ind = 0
    for i in range(n):
        if fuel == 0:
            return F, P
        if fuel > 0:
            F[i] = True
            fuel -= 1
            P[i] = p_ind
        if A[i] > fuel:
            fuel = A[i]
            p_ind = i
    return F, P


def check(A, n):
    F, P = jumpgame(A, n)
    print(A)
    print("is it possible to reach end?: ", F[n-1])
    if F[n-1]:
        i = n-1
        while i != 0:
            print(i, "<- ", end='')
            i = P[i]
        print(i)


A = [1, 1, 0, 2, 0, 2, 2, 2, 2]
# A = [1, 2, 0, 3, 0, 0]
# A = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
n = len(A)

check(A, n)
