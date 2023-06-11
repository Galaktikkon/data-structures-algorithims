class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


# posortowana tablica, x - liczba > 0, czy istnieją takie i,j, że T[j]-T[i]=x

def exists(T, x):
    i = 0
    j = i+1
    while j < len(T):
        if T[i]-T[j] == x:
            return True, i, j
        if T[i]-T[j] < x:
            j += 1
        else:
            i += 1
    return False

# wyrzucenie max z linked listy


def extractmax(L):
    M = L
    while L.next is not None:
        if L.next.val > M.next.val:
            M = L
        L = L.next
    R = M.next
    M.next = R.next
    return R

# znajdowanie min i max w zlozonosci 3/2n


def minmax(T):
    n = len(T)
    gus = T[-1]
    zus = T[-1]
    for i in range(1, n, 2):
        if T[i] < T[i-1]:
            mi, ma = T[i], T[i-1]
        else:
            mi, ma = T[i-1], T[i]
        gus = min(gus, mi)
        zus = max(zus, ma)
    return gus, zus


def insert(T, node):
    pass


def insertion_sort(head):
    S = Node(None)
    while head.next is not None:
        temp = head.next
        head.next = temp.next
        insert(S, temp)
    head.next = S.next
