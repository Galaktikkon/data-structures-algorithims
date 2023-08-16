def longestIdealString(s, k):
    F = [0 for _ in range(26)]
    ans = -1
    for c in s:
        i = ord(c)-ord('a')
        F[i] += 1
        for j in range(max(0, i-k), min(26, i+k+1)):
            if j != i:
                F[i] = max(F[j]+1, F[i])
            ans = max(F[i], ans)
        print(c, F)
    print(F, ans)
    return ans

# s = "acfgbd"
# k = 2


s = "abcd"
k = 3

# s = "azzzaaa"
# k = 0

s = "pvjcci"
k = 4

# s = "lkpkxcigcs"
# k = 6

s = "azaza"
k = 25

s = "dll"
k = 0

longestIdealString(s, k)
