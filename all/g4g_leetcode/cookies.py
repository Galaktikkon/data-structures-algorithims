from math import inf


def distributeCookies(cookies, k):
    F = [0 for _ in range(k)]
    kids = k
    poss_sum = inf

    def f(F, cookies, i):
        nonlocal kids, poss_sum
        if i == len(cookies):
            poss_sum = min(poss_sum, max(F))
            print(F)
            return
        for p in range(kids):
            F[p] += cookies[i]
            f(F, cookies, i+1)
            F[p] -= cookies[i]

    f(F, cookies, 0)

    return poss_sum


cookies = [8, 15, 10, 20, 8]
k = 2

print(distributeCookies(cookies, k))
