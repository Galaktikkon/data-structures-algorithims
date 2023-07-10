from egzP2btesty import runtests
from math import log10
import bisect


def kryptograf(D, Q):
    # tutaj proszę wpisać własną implementację
    result = 1
    q = len(Q)
    n = len(D)
    for i in range(n):
        D[i] = D[i][::-1]
    for i in range(q):
        Q[i] = Q[i][::-1]
    D.sort()

    for i in range(q):
        left = bisect.bisect_left(D, Q[i])
        right = bisect.bisect_right(D, Q[i]+"2")
        result *= right-left

    return log10(result)


D = ["1100", "100", "0", "1111", "1101"]
Q = ["", "1", "11", "0", "1101"]

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests=3)
