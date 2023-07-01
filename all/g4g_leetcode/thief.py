def FindMaxSum(a, n):
    F = [0 for _ in range(n)]
    F[0] = a[0]
    if n > 2:
        F[1] = max(a[0], a[1])

        for i in range(2, n):
            F[i] = max(F[i-1], F[i-2]+a[i])

    return F


a = [5, 5, 10, 100, 10, 5]
a = [1, 2, 3]
a = [2]
n = len(a)


def check(a, n):
    F = FindMaxSum(a, n)
    print(a)
    print(F)
    print("max possible sum is: ", F[n-1])


check(a, n)
