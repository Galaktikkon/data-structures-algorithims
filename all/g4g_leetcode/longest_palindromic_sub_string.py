def longestPalin(S):
    n = len(S)
    F = [[0 for _ in range(n)] for _ in range(n)]
    max_pal = 1
    max_i = 0
    max_j = 0
    for s in range(n):
        i = 0
        j = i+s
        while j < n:
            if i == j:
                F[i][j] = 1
            elif j-i == 1 and S[i] == S[j]:
                F[i][j] = 2
            else:
                if S[i] == S[j] and F[i+1][j-1]:
                    F[i][j] = F[i+1][j-1]+2
            if max_pal < F[i][j]:
                max_i = i
                max_j = j
                max_pal = F[i][j]
            i += 1
            j += 1

    return F, max_pal, S[max_i:max_j+1]


S = "aaaaa"
# S = "abc"
# S = "ab"
# S = "a"
# S = "aaaa"
# S = 'rfkqyuqfjkxy'
# S = 'vnrtysfrzrmzlygfv'
# S = "qrrc"
# S = "ayaxzfbjbkrxiri"
# S = "kjqlrzzfmlvyoshiktodnsjjp"


def check(S):
    res = longestPalin(S)
    print("   ", end='')
    for l in S:
        print(l, " ", end='')
    print()
    for i in range(len(S)):
        print(S[i], res[0][i])
    print("lenght:", res[1])
    print("string:", res[2])


check(S)
