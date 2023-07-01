# Czarodziej Pascal ma N stosów porcelanowych talerzy, przy czym każdy stos zawiera dokładnie k talerzy.
# Pascal wystawia dziś wieczorem kolację na P gości i jedzenie będzie serwowane na tych właśnie talerzach.
# Każdy talerz ma pewne piękno określone liczbą całkowitą. Pomóż czarodziejowi wybrać dokładnie P talerzy tak,
# aby miały one maksymalne piękno. Uwaga! Stos to stos, więc jeśli chcesz zabrać jakiś talerz, to musisz zabrać
# też wszystkie talerze nad nim.


def prefix_sum(A):
    n = len(A)
    P = [0 for _ in range(n)]
    P[0] = A[0]
    for i in range(1, n):
        P[i] = P[i-1]+A[i]
    return P


S = [[1, 0, 2],
     [2, -1, 1],
     [1, 0, 3]]
p = 4


def plates(S, p):
    n = len(S)
    F = [[0 for _ in range(p)] for _ in range(n)]
    P = [prefix_sum(S[i]) for i in range(n)]
    for i in range(p):
        if i > n-1:
            F[0][i] = F[0][i-1]
        else:
            F[0][i] = P[0][i]

    for i in range(1, n):
        F[i][0] = max(F[i-1][0], S[i][0])

    for s in range(1, n):
        for t in range(1, p):
            for i in range(t+1):
                if i < n:
                    p_sum = P[s][i]
                else:
                    p_sum = P[s][len(P[s])-1]
                F[s][t] = max(F[s][t], F[s-1][t-i]+p_sum)

    return F


def check(S, p):
    F = plates(S, p)
    for i in F:
        print(i)


check(S, p)
