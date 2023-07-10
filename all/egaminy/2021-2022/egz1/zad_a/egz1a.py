from egz1atesty import runtests


def right(i): return 2*i+2
def left(i): return 2*i+1
def parent(i): return (i-1)//2


def heapify(A, i, n):
    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)


def buildHeap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, i, n)


def snow(S):
    # tu prosze wpisac wlasna implementacje

    n = len(S)
    snowSum = 0
    melt = 0
    i = n-1

    buildHeap(S)

    while S[0]-melt > 0:

        snowSum += S[0]-melt

        S[0], S[i] = S[i], S[0]

        S.pop(len(S)-1)

        heapify(S, 0, i)

        melt += 1
        i -= 1

    return snowSum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
