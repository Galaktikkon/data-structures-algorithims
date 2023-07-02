def CountWays(str):
    n = len(str)
    F = [0 for _ in range(n+1)]
    F[0] = 1
    for s in range(1, n+1):
        pass

    return F


str = "123"


def check(str):
    F = CountWays(str)
    print(F)


check(str)
