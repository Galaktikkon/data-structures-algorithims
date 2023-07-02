def perfectSum(arr, n, psum):

    F = [[0 for _ in range(n+1)] for _ in range(psum+1)]

    Z = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if arr[i-1] == 0:
            Z[i] += Z[i-1]+1
        else:
            Z[i] += Z[i-1]

    for i in range(n+1):
        F[0][i] = pow(2, Z[i])

    mod = pow(10, 9)+7

    for i in range(1, psum+1):
        for j in range(1, n+1):
            if i-arr[j-1] >= 0:
                F[i][j] = (F[i-arr[j-1]][j-1] % mod + F[i][j-1] % mod) % mod
            else:
                F[i][j] = F[i][j-1]

    return F


psum = 10
arr = [2, 3, 5, 6, 8, 10]
n = len(arr)


def check(arr, n, psum):
    F = perfectSum(arr, n, psum)
    print("     ", arr)
    print("    ", end='')
    for i in range(n+1):
        print(i, " ", end='')
    print()
    for i in range(psum+1):
        print(f'{i:2}', F[i])


check(arr, n, psum)
