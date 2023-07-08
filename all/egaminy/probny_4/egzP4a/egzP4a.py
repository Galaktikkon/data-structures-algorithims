from egzP4atesty import runtests


T = [(1, 2), (2, 3), (3, 0)]


def mosty(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    T.sort(key=lambda x: x[0])
    F = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if T[i][1] >= T[j][1] and F[j]+1 > F[i]:
                F[i] = F[j]+1

    return max(F)


runtests(mosty, all_tests=True)
