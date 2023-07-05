from zad6ktesty import runtests


def haslo(S):
    n = len(S)
    F = [0 for _ in range(n+1)]
    F[0] = 1
    for s in range(1, n+1):
        if S[s-1] != "0":
            if S[s-2] == "1" or (S[s-2] == "2" and S[s-1] < "7"):
                F[s] += F[s-2]
            if "1" <= S[s-1] <= "9":
                F[s] += F[s-1]
        else:
            if S[s-2] == "2" or S[s-2] == "1":
                F[s] += F[s-2]
            else:
                return 0
    return F[n]


S = '36671106'

print(haslo(S))

# runtests(haslo)
