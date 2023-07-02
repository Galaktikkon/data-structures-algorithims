def longestCommonSubstr(S1, S2, n, m):
    F = [[0 for _ in range(m+1)] for _ in range(n+1)]

    max_len = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if S1[i-1] == S2[j-1]:
                if F[i-1][j-1] > 0:
                    F[i][j] = F[i-1][j-1]+1
                else:
                    F[i][j] = 1
            max_len = max(max_len, F[i][j])
    return F, max_len


S1 = "BCDYGHRE"
S2 = "ABCDXGHRE"
# S1 = "ABC"
# S2 = "DEF"


n = len(S1)
m = len(S2)


def check(S1, S2, n, m):
    F = longestCommonSubstr(S1, S2, n, m)
    for i in F[0]:
        print(i)
    print("lenght of the common substring:", F[1])


check(S1, S2, n, m)
