from egzP6atesty import runtests


def partition(A, p, r):

    x = A[r]

    i = p-1

    for j in range(p, r):
        if A[j][1] == x[1]:
            if A[j][2] >= x[2]:
                i += 1
                A[j], A[i] = A[i], A[j]
        elif A[j][1] > x[1]:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1


def select(A, k, p, r):

    q = partition(A, p, r)

    if q == k:
        return A[q]

    elif q > k:
        return select(A, k, p, q-1)

    elif q < k:
        return select(A, k, q+1, r)


def convert(S):
    letter_count = 0
    for l in S:
        if 'a' <= l <= 'z':
            letter_count += 1
    return (len(S), letter_count)


H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
s = 3


def google(H, s):
    # tutaj proszę wpisać własną implementację
    n = len(H)
    P = []
    for i in range(n):
        d, l = convert(H[i])
        P.append((H[i], d, l))
    i = select(P, s-1, 0, n-1)

    return i[0]  # type: ignore


# print(google(H, s))

runtests(google, all_tests=True)
