def cutRod(price, n):
    # code here
    F = [0 for _ in range(n+1)]
    for p in range(n):
        F[p] = price[0]*p
    for i in range(n):
        for p in range(1, n+1):
            F[p] = max(F[p-1], F[p])
            if i+1 <= p:
                F[p] = max(F[p], F[p-i-1]+price[i])
    return F


# P = [1, 5, 8, 9, 10, 17, 17, 20]
P = [3, 5, 8, 9, 10, 17, 17, 20]
n = len(P)


def check(P, n):
    F = cutRod(P, n)
    print(F)
    print("maximum price is: ", F[n])


check(P, n)
