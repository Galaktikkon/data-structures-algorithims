from zad3testy import runtests


def intersect(a, b):
    x1, y1 = a
    x2, y2 = b
    new_min = max(x1, x2)
    new_max = min(y1, y2)
    if new_min <= new_max:  # type: ignore
        return (new_min, new_max)
    return (0, 0)


def section_len(a):
    return a[1]-a[0]


def kintersect(A, k):
    from math import inf
    A.append((-inf, inf))
    n = len(A)
    F = [[(-1, -1) for _ in range(k+2)] for _ in range(n)]

    def f(F, A, k, i):

        if F[i][k] != (-1, -1):
            return F[i][k]
        if i < k-1:
            F[i][k] = (0, 0)
            return (0, 0)
        if k == 1:
            F[i][k] = A[i]
            return A[i]

        res = (0, 0)

        for j in range(i):
            if section_len(intersect(A[i], f(F, A, k-1, j))) > section_len(res):
                res = intersect(A[i], f(F, A, k-1, j))

        F[i][k] = res

        return F[i][k]

    f(F, A, k+1, n-1)

    # for i in F:
    # print(i)
    max_sec = (-inf, inf)
    num = k
    sol = []

    for i in range(n-1, -1, -1):
        if num == 0:
            break
        idx = -1
        sec = (0, 0)
        for j in range(i):
            if section_len(intersect(sec, max_sec)) < section_len(intersect(F[j][num], max_sec)):
                sec = F[j][num]
                idx = j

        if idx != -1 and sec != (-inf, inf):
            sol.append(idx)
            max_sec = sec
        num -= 1
    print(section_len(F[n-1][k+1]), 'moj wynik')
    # print(sorted(sol))
    return sorted(sol)


A = [(0, 4), (1, 10), (6, 7), (2, 8)]
k = 3
# A = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]
# k = 3
# A = [(x, x + 2) for x in range(50)]
# k = 2


kintersect(A, k)
runtests(kintersect)
