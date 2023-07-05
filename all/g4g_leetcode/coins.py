def count(coins, N, Sum):
    # code here
    F = [[0 for _ in range(Sum+1)] for _ in range(N+1)]
    # beg cond
    for i in range(N+1):
        F[i][0] = 1
    for s in range(Sum+1):
        F[0][s] = 1
    for s in range(Sum+1):
        if s % coins[0] == 0:
            F[1][s] = 1
    for i in range(2, N+1):
        for s in range(1, Sum+1):
            F[i][s] = F[i-1][s]
            if s >= coins[i-1]:
                F[i][s] = F[i-1][s]+F[i][s-coins[i-1]]
    return F


coins = [3, 2, 1]
Sum = 4
coins = [1, 1, 1, 1]
Sum = 4


def del_dups(A):
    res = [*set(A)]
    return res


def check(A, s):
    A = del_dups(A)
    F = count(A, len(A), s)
    for i in F:
        print(i)
    print("number of distinct combinations: ", F[len(A)][s])


check(coins, Sum)
