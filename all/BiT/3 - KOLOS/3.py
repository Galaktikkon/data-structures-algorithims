# pomysł - quickSelect na p-tej pozycji, a pozniej na q-tej, ale od p do konca
# ważne i ciekawe konekwencje quickSelecta !
# na początku quickSelect na p-tej pozycji, wywali wszystko mniejsze od p na początek tablicy, a większe na koniec,
# dalej jak użyjemy quickSelecta na q-tej pozycji, ALE na indeksach od p do końca tablicy, to w efekcie, na prawo od q
# będą elementy mniejzse od q, ale z konsekwencji użycia quickSelecta z p wcześniej, będą one również większe od p
# czyli szukany przedział został znaleziony

def partition(A, p, r):

    x = A[r]

    i = p-1

    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[r], A[i+1] = A[i+1], A[r]

    return i+1


def quickSelect(A, p, r, k):

    q = partition(A, p, r)

    if q == k:
        return A[q]
    elif q > k:
        return quickSelect(A, p, q-1, k)
    elif q < k:
        return quickSelect(A, q+1, r, k)


def section(T, p, q):

    n = len(T)
    quickSelect(T, 0, n-1, p)
    quickSelect(T, p, n-1, q)

    return T[p:q+1]


T = [9, 8, 4, 2, 3, 5, 7, 1, 6]

print(section(T, 2, 4))
