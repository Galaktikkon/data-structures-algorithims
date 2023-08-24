from zad2testy import runtests


class Node:
    def __init__(self, left=None, leftval=0, right=None, rightval=0):
        self.left = left  # lewe podrzewo
        self.leftval = leftval  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = right  # prawe poddrzewo
        self.rightval = rightval  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def writeTree(T):
    A = []
    tree_index = 0

    def dfs(T, A):
        if T is None:
            return
        nonlocal tree_index
        A.append(T)
        T.X = tree_index
        tree_index += 1

        if T.left != None:
            dfs(T.left, A)
        if T.right != None:
            dfs(T.right, A)

    dfs(T, A)

    return A


def valuableTree(T, k):
    from math import inf
    A = writeTree(T)
    n = len(A)

    if k == 0:
        return 0
    if not T or n-1 < k:
        return None

    F = [[-1 for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        F[i][0] = 0

    def f(F, root, k):
        if F[root.X][k] != -1:
            return F[root.X][k]

        res = -inf

        if root.right != None:
            res = max(res, f(F, root.right, k-1)+root.rightval)

        if root.left != None:
            res = max(res, f(F, root.left, k-1)+root.leftval)

        if root.left != None and root.right != None and k >= 2:
            for j in range(k-1):
                res = max(res, f(F, root.left, j) +
                          root.leftval+f(F, root.right, k-j-2)+root.rightval)

        F[root.X][k] = res

        return F[root.X][k]

    sol = -inf
    for i, root in enumerate(A):
        f(F, root, k)
        sol = max(sol, F[i][k])

    return sol


runtests(valuableTree)
