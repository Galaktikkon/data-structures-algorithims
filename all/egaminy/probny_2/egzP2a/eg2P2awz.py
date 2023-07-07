from egzP2atesty import runtests


def partition(C, A, p, r):

    x = A[C[r]][1]

    i = p-1

    for j in range(p, r):
        if A[C[j]][1] >= x:
            i += 1
            A[C[j]], A[C[i]] = A[C[i]], A[C[j]]
    A[C[r]], A[C[i+1]] = A[C[i+1]], A[C[r]]

    return i+1


def select(C, A, k, p, r):

    q = partition(C, A, p, r)
    if q > k:
        return select(C, A, k, p, q-1)

    elif q < k:
        return select(C, A, k, q+1, r)
    return


T = [1, 2, 4, 3, 6, 7, 4, 8, 11, 9, 10, 0]


def zdjecie(T, m, k):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    convert = [0 for _ in range(n)]
    pointer = k+m-1
    start = [0 for _ in range(m)]
    end = [0 for _ in range(m)]
    for i in range(m):
        if i == 0:
            end[i] = pointer-1
        else:
            start[i] = end[i-1]+1
            end[i] = start[i]+pointer-1
        pointer -= 1
    people = 0
    col = 0
    row = 0
    while people < n:
        while row < m and col+start[row] <= end[row]:
            convert[start[row]+col] = people
            row += 1
            people += 1
        row = 0
        col += 1
    r = end[m-1]
    for i in range(m-2, -1, -1):
        select(convert, T, end[i], 0, r)
        r = end[i]-1
    return None


runtests(zdjecie, all_tests=True)
