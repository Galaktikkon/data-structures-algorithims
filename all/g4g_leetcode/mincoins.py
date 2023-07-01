def minCoins(coins, M, V):
    # code here
    from math import inf
    F = [-1 for _ in range(V+1)]
    F[0] = 0

    def rec_coins(coins, M, V, F):
        res = inf
        if V == 0:
            return 0
        if F[V] != -1:
            return F[V]
        for j in range(M):
            if coins[j] <= V:
                sub_res = rec_coins(coins, M, V-coins[j], F)
                if sub_res != -1 and sub_res+1 < res:
                    res = sub_res+1

        F[V] = res if res != inf else -1

        return res

    rec_coins(coins, M, V, F)
    return F


V = 39
coins = [9, 2, 11, 5, 14, 17, 8, 18]
M = len(coins)


def check(coins, M, V):
    print("amount of money: ", end='')
    for i in range(V+1):
        print(f'{i:2}', end=' ')
    print()
    F = minCoins(coins, M, V)
    print("number of coins: ", end='')
    for i in range(V+1):
        print(f'{F[i]:2}', end=' ')
    # print("\nminimum number of coins to obtain", V, "is", F[V])


print(minCoins(coins, M, V))
check(coins, M, V)
