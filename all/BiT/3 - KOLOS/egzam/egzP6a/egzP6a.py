from egzP6atesty import runtests


def partition(A, p, r):

    x = A[r][1]

    i = p-1

    for j in range(p, r):
        if A[j][1] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quickSelect(A, p, r, k):

    q = partition(A, p, r)

    if q == k:
        return A[q][0]
    elif q > k:
        return quickSelect(A, p, q-1, k)
    elif q < k:
        return quickSelect(A, q+1, r, k)


def letterCount(s):
    counter = 0
    for letter in s:
        if ord(letter) > 57:
            counter += 1
    return counter


def convert(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], 10*len(T[i])+letterCount(T[i]))


def google(H, s):
    # tutaj proszę wpisać własną implementację
    n = len(H)
    convert(H)
    return quickSelect(H, 0, n-1, n-s)


H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
print(google(H, 3))
# print(H)
# runtests ( google, all_tests=True )
