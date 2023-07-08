from egzP4btesty import runtests


class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def find_max(N):
    while N.left:
        N = N.left
    return N.key


def find_min(N):
    while N.right:
        N = N.right
    return N.key


def pred(N):
    if N.left:
        return find_min(N.left)
    ptr = N.parent
    while ptr.parent != None and ptr.right != N:
        N = ptr
        ptr = ptr.parent
    return ptr.key


def succ(N):
    if N.right:
        return find_max(N.right)
    ptr = N.parent
    while ptr.parent != None and ptr.left != N:
        N = ptr
        ptr = ptr.parent
    return ptr.key


def sol(root, T):
    result = 0
    for node in T:
        p = pred(node)
        s = succ(node)
        if p+s == 2*node.key:
            result += node.key

    return result


runtests(sol, all_tests=True)
