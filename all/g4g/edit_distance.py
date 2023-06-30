def edit_distance(s, t):
    from math import inf
    n = len(s)
    m = len(t)
    F = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for j in range(1, n+1):
        F[0][j] = j
    for i in range(1, m+1):
        F[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            a, b, c = inf, inf, inf
            b = F[i][j-1]+1
            a = F[i-1][j]+1
            if t[i-1] != s[j-1]:
                c = F[i-1][j-1]+1
            else:
                c = F[i-1][j-1]
            F[i][j] = min(a, b, c)

    return F


def check(s, t):
    F = edit_distance(s, t)
    for i in F:
        print(i)
    print("minimum number of operations is: ", F[len(t)][len(s)])


s = "geek"
t = "gesek"

s = "gfg"
t = "gfg"

s = "dsa"
t = "asd"

check(s, t)
