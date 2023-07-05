def maximizeTheCuts(n, x, y, z):
    cut = [*set([x, y, z])]
    l = len(cut)
    F = [[[0, 0] for _ in range(n+1)] for _ in range(l+1)]
    for i in range(n+1):
        F[1][i][0] = i//cut[0]
        F[1][i][1] = i % cut[0]
    for c in range(2, l+1):
        for i in range(1, n+1):
            F[c][i][0] = i//cut[c-1]
            F[c][i][1] = i % cut[c-1]
            if F[c-1][F[c][i][1]][1] == 0:
                F[c][i][0] += F[c-1][F[c][i][1]][0]
                F[c][i][1] = 0
            if F[c][i][0] < F[c-1][i][0] and F[c-1][i][1] == 0:
                F[c][i][1] = F[c-1][i][1]
                F[c][i][0] = F[c-1][i][0]

    return F, F[l][n]


x = 5
y = 5
z = 2
n = 7

# x = 5
# y = 3
# z = 2
# n = 5


def check(x, y, z, n):
    F = maximizeTheCuts(n, x, y, z)
    for i in F[0]:
        print(i)
    print("maximized number of cuts: ", F[1])


check(x, y, z, n)

# print(maximizeTheCuts(n, x, y, z))
