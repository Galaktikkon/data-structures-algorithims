from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def get_len(W):
    l = 0
    while W != None:
        W = W.next
        l += 1
    return l


def kp(W):
    n = get_len(W)
    p = W.fundusze
    F = [[0 for _ in range(p+1)] for _ in range(n)]
    ptr = W
    for b in range(ptr.koszt, p):
        F[0][b] = ptr.wyborcy
    for b in range(p+1):
        ptr = W.next
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            if b-ptr.koszt >= 0:
                F[i][b] = max(F[i][b], F[i-1][b-ptr.koszt]+ptr.wyborcy)
            ptr = ptr.next
    return F[n-1][p]


def wybory(T):
    # tutaj proszę wpisać własną implementację
    result = 0
    for W in T:
        result += kp(W)
    return result


runtests(wybory, all_tests=True)
