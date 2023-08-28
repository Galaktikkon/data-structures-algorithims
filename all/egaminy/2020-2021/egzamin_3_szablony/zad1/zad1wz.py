from zad1testy import runtests


def bisect_left_inc(a, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def bisect_left_dec(a, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# dec[i] - pod i-tym indeksem jest najmniejsza wartość, która kończy ciąg o długości i


def mr(X):
    n = len(X)
    dec_size = 1
    inc_size = 1
    dec = [i for i in range(n+1)]
    inc = [n-i for i in range(n+1)]
    F = [1 for _ in range(n)]
    G = [1 for _ in range(n)]
    F_parent = [-1 for _ in range(n)]
    for i in range(1, n):
        if X[i] > dec[1]:
            dec[1] = X[i]  # type: ignore
            F[i] = 1
        elif X[i] < dec[dec_size]:
            dec[dec_size+1] = X[i]  # type: ignore
            F_parent[i] = dec[dec_size]
            F[i] = dec_size+1
            dec_size += 1
        else:
            k = bisect_left_dec(dec, X[i], 1, dec_size)
            dec[k] = X[i]  # type: ignore
            F[i] = k
            F_parent[i] = dec[k-1]
    for i in range(n-1, -1, -1):
        if X[i] > inc[n-1]:
            inc[n-1] = X[i]
            G[i] = 1
        elif X[i] < inc[n-inc_size]:
            inc[n-inc_size-1] = X[i]
            G[i] = inc_size+1
            inc_size += 1
        else:
            k = bisect_left_inc(inc, X[i], n-inc_size, n-1)
            # print(k, inc[k], inc[k+1], X[i], n-inc_size, n-1)
            inc[k] = X[i]
            G[i] = n-k
    print(dec)
    # print(inc)
    print(F)
    # print(F_parent)
    # print(G)

    return []


X = [4, 10, 5, 1, 5, 2, 3, 4]
# X = [1, 3, 2, 1]
# X = [1, 2, 3, 4, 5]
# X = [2, 5, 3, 2, 1, 23, 5, 7, 8, 5, 4, 3, 21, 2, 3, 4, 5, 7, 3]
mr(X)
# runtests(mr)
