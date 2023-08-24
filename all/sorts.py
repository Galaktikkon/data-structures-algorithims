def partition(A, p, r):

    x = A[r]

    i = p-1

    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1


def quickSort2(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quickSort2(A, p, q-1)
        p = q+1


def select(A, k, p, r):

    q = partition(A, p, r)

    if q == k:
        return A[q]

    elif q > k:
        return select(A, k, p, q-1)

    elif q < k:
        return select(A, k, q+1, r)


def countingSort(A, k):
    n = len(A)

    C = [0]*k
    B = [0]*n

    for i in range(n):
        C[A[i]] += 1

    for i in range(1, k):
        C[i] = C[i]+C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B

# MERGE SORT


def merge(A, left, mid, right, index):

    n1 = mid-left+1
    n2 = right-mid

    L = [(0, 0) for _ in range(n1)]
    R = [(0, 0) for _ in range(n2)]

    for i in range(n1):
        L[i] = A[i+left]

    for i in range(n2):
        R[i] = A[i+mid+1]

    sortIndex = left
    i, j = 0, 0

    while i < n1 and j < n2:
        if L[i][index] <= R[j][index]:
            A[sortIndex] = L[i]
            i += 1
        else:
            A[sortIndex] = R[j]
            j += 1
        sortIndex += 1

    while i < n1:
        A[sortIndex] = L[i]
        i += 1
        sortIndex += 1
    while j < n2:
        A[sortIndex] = R[j]
        j += 1
        sortIndex += 1


def mergeSort(A, left, right, index):
    if left < right:
        mid = (left+right)//2
        mergeSort(A, left, mid, index)
        mergeSort(A, mid+1, right, index)
        merge(A, left, mid, right, index)
