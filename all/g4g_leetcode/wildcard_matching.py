def isMatch(s, p):
    n = len(s)
    m = len(p)
    F = {}

    def f(F, s, p, i, j):
        nonlocal n, m

        if (i, j) in F:
            return F[(i, j)]

        if i >= n and j >= m:
            F[(i, j)] = True
            return F[(i, j)]

        if j >= m:
            F[(i, j)] = False
            return F[(i, j)]

        flag = i < n and (s[i] == p[j] or p[j] == "?")

        if p[j] == "*" and i <= n:
            F[(i, j)] = f(F, s, p, i+1, j) or f(F, s, p, i, j+1)
            return F[(i, j)]

        if flag:
            F[(i, j)] = f(F, s, p, i+1, j+1)
            return F[(i, j)]
        else:
            F[(i, j)] = False
            return F[(i, j)]

    return f(F, s, p, 0, 0)


s = "aa"
p = "a"

# s = "aa"
# p = "*"

# s = "cb"
# p = "?a"

# s = "acdcb"
# p = "a*c?b"

assert isMatch("aa", "a") == False
assert isMatch("aa", "*") == True
assert isMatch("cb", "?a") == False
assert isMatch("acdcb", "a*c?b") == False

print(isMatch(s, p))
