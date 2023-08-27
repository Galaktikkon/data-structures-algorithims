from zad3testy import runtests
from math import log2, floor


class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.right = None  # prawe poddrzewo
        self.parent = None  # rodzic drzewa jesli istnieje
        self.key = None  # klucz


def bin_find(T, idx, level, root):
    if level == 0:
        return T.key
    if idx < root*pow(2, level)+pow(2, level-1):
        return bin_find(T.left, idx, level-1, root*2)
    else:
        return bin_find(T.right, idx, level-1, root*2+1)


def maxim(T, C):
    """tu prosze wpisac wlasna implementacje"""
    from math import inf
    sol = -inf
    for idx in C:
        sol = max(sol, bin_find(T, idx, floor(log2(idx)), 1))

    return sol


runtests(maxim)
