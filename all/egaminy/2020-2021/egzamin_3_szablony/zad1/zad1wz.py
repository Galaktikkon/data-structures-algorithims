from zad1testy import runtests


def bisect_left_inc(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_left_dec(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def mr(X):
    n = len(X)
    dec = [X[0]]
    inc = [X[0]]
    F = [1 for _ in range(n)]
    G = [1 for _ in range(n)]
    for i in range(1, n):
        if X[i] < dec[-1]:
            dec.append(X[i])
        else:
            dec[bisect_left_dec(dec, X[i])] = X[i]

    print(dec)
    # print(inc)
    print(F)
    # print(G)

    return []


X = [4, 10, 5, 1, 5, 2, 3, 4]

mr(X)
# runtests(mr)
