from zad1testy import runtests


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


def chaos_index(T):
    k = 0
    n = len(T)
    # tu prosze wpisac wlasna implementacje
    ind_T = [[T[i], i] for i in range(n)]
    mergeSort(ind_T, 0, n-1, 0)
    print(ind_T)
    for i in range(n):
        k = max(k, abs(i-ind_T[i][1]))
    return k


# T = [0, 2, 1.1, 2]

# chaos_index(T)

runtests(chaos_index)
