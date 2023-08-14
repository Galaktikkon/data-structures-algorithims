def longestIdealString(s, k):
    n = len(s)
    F = [0 for _ in range(n+1)]
    F[1] = 1
    for i in range(2, n+1):
        if abs(ord(s[i-1])-ord(s[i-2])) <= k:
            F[i] = F[i-1]+1


s = "acfgbd"
k = 2

# s = "abcd"
# k = 3

# s = "azzzaaa"
# k = 0

longestIdealString(s, k)
