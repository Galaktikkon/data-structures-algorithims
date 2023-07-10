from egzP8atesty import runtests
from bisect import bisect_right
T = [(0, 3), (4, 5), (1, 4)]
S = [5000, 3000, 15000]
o = 6


def reklamy(T, S, o):
    # Tutaj proszę wpisać własną implementację
    result = 0
    n = len(S)
    A = []
    for i in range(n):
        A.append((T[i][0], T[i][1], S[i]))
    A.sort(key=lambda x: x[0])
    F = [0 for _ in range(n)]
    F[-1] = A[-1][2]
    for i in range(n-2, -1, -1):
        F[i] = max(F[i+1], A[i][2])

    S = [A[i][0] for i in range(n)]

    for i in range(n):
        end_idx = A[i][1]
        idx = bisect_right(S, end_idx, i+1)

        second = 0
        if idx < n and S[idx] != end_idx:
            second = F[idx]
        result = max(result, A[i][2]+second)
    return result


runtests(reklamy, all_tests=True)
