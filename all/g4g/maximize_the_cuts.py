def maximizeTheCuts(n, x, y, z):
    F = [-1 for _ in range(n+1)]
    F[0] = 0
    for i in range(1, n+1):
        a, b, c = -1, -1, -1
        if x <= i and F[i-x] >= 0:
            a = F[i-x]+1
        if y <= i and F[i-y] >= 0:
            b = F[i-y]+1
        if z <= i and F[i-z] >= 0:
            c = F[i-z]+1
        F[i] = max(a, b, c)
    return F


x = 2
y = 1
z = 1
n = 4

# x = 5
# y = 3
# z = 2
# n = 5


def check(x, y, z, n):
    F = maximizeTheCuts(n, x, y, z)
    print(F)
    print("maximized number of cuts: ", F[n])


check(x, y, z, n)

# print(maximizeTheCuts(n, x, y, z))
