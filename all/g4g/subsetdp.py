def isSubsetSum(N, arr, s):
    # code here
    F = [[False for _ in range(s+1)] for _ in range(N)]
    for i in range(N):
        F[i][0] = True
    F[0][arr[0]] = True
    for i in range(1, N):
        for j in range(s+1):
            if j-arr[i] >= 0:
                F[i][j] = F[i-1][j] or F[i-1][j-arr[i]]
            else:
                F[i][j] = F[i-1][j]
    return F[N-1][s]


N = 6
arr = [300, 34, 4, 12, 5, 2]
s = 9

# A = isSubsetSum(N, arr, s)
# for i in A:
#     print(i)
print(isSubsetSum(N, arr, s))
