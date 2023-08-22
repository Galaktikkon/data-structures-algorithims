def isMatch(s, p):
    n = len(s)
    m = len(p)
    F = {}

    def f(F, s, p, i, j):
        nonlocal n, m

        if (i, j) in F:
            return F[(i, j)]

        if i >= n and j >= m:
            print('xd')
            F[(i, j)] = True
            return F[(i, j)]
        if j >= m:
            F[(i, j)] = False
            return F[(i, j)]

        if i < n and (s[i] == p[j] or p[j] == "."):
            flag = True
        else:
            flag = False

        if j+1 < m and p[j+1] == "*":
            if flag:
                F[(i, j)] = f(F, s, p, i+1, j) or f(F, s, p, i, j+2)
                return F[(i, j)]
            else:
                F[(i, j)] = f(F, s, p, i, j+2)
                return F[(i, j)]
        else:
            if flag:
                F[(i, j)] = f(F, s, p, i+1, j+1)
                return F[(i, j)]
            else:
                F[(i, j)] = False
                return F[(i, j)]

    return f(F, s, p, 0, 0)


s = "abc"
p = "a*b*abc"

isMatch(s, p)


# assert isMatch("aa", "a") == False
# assert isMatch("aa", "a*") == True
# assert isMatch("ab", ".*") == True
