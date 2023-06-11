# 1. quicksort w pamięci O(logn)
# 2. quicksort bez rekurencji, z własnym stosem
# 3. wstawianie do kopca binarnego
# 4. k posortowanych list, chcemy scalić w jedną
# 5. struktura danych z operacjami:
# insert, extractMin, extractMax - O(logn)
# 6. struktura danych z operacjami:
# insert, extractMedian - O(logn)

# 1:

def partition(A, p, r):

    x = A[r]

    i = p-1

    for k in range(p, r):
        if A[k] <= x:
            i += 1
            A[i], A[k] = A[k], A[i]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1


def quickSort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        # wybor mniejsze czesci, ktora maksymalnie zajmnie logn
        if q-p < r-q:
            quickSort(A, p, q-1)
            r = q+1
        else:
            quickSort(A, q+1, r)
            r = q-1

# 3:


class Heap:
    def __init__(self, n):
        self.T = [0]*n
        self.size = 0


def insert(H, x):
    i = H.size
    p = parent(H.size)
    H.T[H.size] = x
    H.size += 1
    while p >= 0:
        if H.T[p] < H.T[i]:
            H.T[p], H.T[i] = H.T[i], H.T[p]
        else:
            break
        i = p
        p = parent(p)


def quickSortIt(A, p, r):
    S = stack()
    S.push((p, r))
    while not S.isEmpty():
        a, b = S.pop()
        S.push()
        if b > a:
            q = partition(A, a, b)
            if q-p < r-q:
                S.push(q+1, b)
            else:
                S.push(a, q-1)
