from egzP4atesty import runtests
import bisect


def mosty(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    T.sort(key=lambda x: x[0])
    S = [T[0][1]]
    for i in range(1, n):
        if T[i][1] >= S[-1]:
            S.append(T[i][1])
        else:
            S[bisect.bisect_left(S, T[i][1])] = T[i][1]
        print(S)

    return len(S)

# runtests(mosty, all_tests=True)
