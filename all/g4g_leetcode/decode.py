def CountWays(str):
    n = len(str)
    F = [0 for _ in range(n+1)]
    F[0] = 1
    for s in range(1, n+1):
        F[s] = F[s-1]

        if str[s-1] == 0 and str[s-2] > 2 or str[s-2] == 2 and str[s-1] > 6:
            F[s-1] = 0

    return F


str = "123"


def check(str):
    F = CountWays(str)
    print(F)


check(str)
