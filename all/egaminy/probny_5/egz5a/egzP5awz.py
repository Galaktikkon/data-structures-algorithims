from egzP5atesty import runtests

T = [2, 1, 5, 6, 2, 3]


def inwestor(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    F = [0 for _ in range(n)]
    F[0] = T[0]
    mi = T[0]
    i = 0
    max_sum = T[0]
    for j in range(1, n):
        mi = min(mi, T[j])
        if mi*(j-i+1) > F[j-1]:
            F[j] = mi*(j-i+1)
        if T[j] > mi*(j-i+1):
            F[j] = T[j]
            mi = T[j]
            i = j
        else:
            F[j] = F[j-1]
    print(T)
    print(F)


inwestor(T)


# runtests(inwestor, all_tests=True)
