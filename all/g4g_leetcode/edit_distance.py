def edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        F[i][0] = i
    for j in range(m+1):
        F[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if word1[i-1] == word2[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1])+1

    return F


def check(s, t):
    F = edit_distance(s, t)
    for i in F:
        print(i)
    print("minimum number of operations is: ", F[len(s)][len(t)])


s = "geek"
t = "gesek"

# s = "gfg"
# t = "gfg"

# s = "dsa"
# t = "asd"

# s = "horse"
# t = "ros"

check(s, t)
