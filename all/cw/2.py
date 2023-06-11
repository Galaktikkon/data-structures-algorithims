class Node:
    def __init__(self, v):
        self.next = None
        self.val = v

# implementacja mergesort dla list jednokierunkowych
    # a) pomysl
    # b) odcinanie
    # c) scalanie dwoch list
    # d) merge

# znajdowanie inwersji w tablicy

# pojemniki z woda, wiemy ile wody jest wlanej, ile jest zalanych>?


# ad 1:

def cut(P):

    if P.next is None:
        return (None, None)
    q = P

    while P.next is not None and P.val <= P.next.val:
        P = P.next

    h = q.next
    q.next = P.next
    P.next = None

    return (h, P)


def merge(p1, p2):

    A = B = Node(None)

    while p1 is not None and p2 is not None:

        if p1.val < p2.val:
            A.next = p1
            p1 = p1.next

        else:
            A.next = p2
            p2 = p2.next

        A = A.next

    while p1 is not None:
        A.next = p1
        p1 = p1.next
        A = A.next

    while p2 is not None:
        A.next = p2
        p2 = p2.next
        A = A.next

    return B.next, A


def mergeSort(A):

    E = A

    while E.next is not None:  # robimy wskaznik na koniec listy
        E = E.next

    while True:

        Ah, At = cut(A)  # odcinamy dwie pierwsze serie naturalne
        Bh, Bt = cut(A)

        if E == Bt:  # wazny warunek bo inaczej po zmergowaniu zrobi sie cykl
            E = A
        if Bh is None:  # jesli drugi kawalek nie istnieje to return
            A.next = Ah
            return
        Mh, Mt = merge(Ah, Bh)  # scalenie i przepiecie koncowki
        E.next = Mh
        E = Mt

# ad 3:

# arr=[((0,10),(10,0)), ... ]

# a) szerokosc aktywna


def water(arr, water):
    pass

# b) bisekcja


def sumWater(arr, level):
    waterSum = 0
    for i, j in arr:
        if i[1] <= level:
            waterSum += (abs(i[1]-j[1])*abs(i[0]-j[0]))
    return waterSum


def bisectSolution(arr, water):

    ma = -float('inf')
    for i, j in arr:
        ma = max(ma, i[1])

    left = 0
    right = ma
    mid = (left+right)//2
    tanks = 0

    while left <= right:

        if water > sumWater(arr, mid) and water > sumWater(arr, mid-1):
            left = mid+1

        elif water < sumWater(arr, mid) and water < sumWater(arr, mid+1):
            right = mid-1

        elif water >= sumWater(arr, mid) and water < sumWater(arr, mid+1):
            break

        mid = (left+right)//2

    for i, j in arr:
        if mid >= i[1]:
            tanks += 1

    return tanks


arr = [((4, 6), (6, 2)), ((8, 8), (20, 4)), ((14, 16), (16, 14)),
       ((16, 12), (20, 10)), ((22, 16), (24, 16)), ((4, 16), (10, 10))]
# arr=[((0,1),(1,0))]

print(bisectSolution(arr, 76))
# print(sumWater(arr,6))

# ad 2

# merge sort [1,2,4,3,1,2,5,4]


def inversions(arr):
    pass
