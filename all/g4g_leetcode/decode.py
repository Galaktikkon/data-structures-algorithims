def CountWays(str):
    n = len(str)
    F = [0 for _ in range(n+1)]
    F[0] = 1
    for s in range(1, n+1):
        if str[s-1] != "0":
            if F[s-1] > 0:
                if str[s-2] == "1" or (str[s-2] == "2" and str[s-1] < "7"):
                    F[s] += F[s-2]
                if "1" <= str[s-1] <= "9":
                    F[s] += F[s-1]
        else:
            if str[s-2] == "2" or str[s-2] == "1":
                F[s] += F[s-1]
            else:
                F[s] = 0
    return F[n]


str = "1233522"


def check(str):
    F = CountWays(str)
    print(F)


check(str)
