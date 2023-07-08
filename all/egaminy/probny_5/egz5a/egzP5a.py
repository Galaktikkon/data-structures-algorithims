from egzP5atesty import runtests

T = [2, 1, 5, 6, 2, 3]


def inwestor(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    F = [[0 for _ in range(n)] for _ in range(n)]
    max_sum = 0
    for i in range(n):
        F[i][i] = T[i]
    for i in range(n):
        a = 0
        b = i+1
        while b < n:
            if a+1 == b:
                F[a][b] = min(T[a], T[b])
            else:
                F[a][b] = min(F[a+1][b], F[a][b-1])
            max_sum = max(max_sum, F[a][b]*(b-a+1))
            b += 1
            a += 1
    return max_sum


# inwestor(T)

runtests(inwestor, all_tests=True)
