from zad1testy import runtests


def mr(X):
    """tu prosze wpisac wlasna implementacje"""

    n = len(X)
    F = [1 for _ in range(n)]
    G = [1 for _ in range(n)]
    F_parent = [-1 for _ in range(n)]
    G_parent = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if X[j] > X[i] and F[j]+1 > F[i]:
                F[i] = F[j]+1
                F_parent[i] = j

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if X[j] > X[i] and G[j]+1 > G[i]:
                G[i] = G[j]+1
                G_parent[i] = j

    # print(F)
    # print(F_parent)
    # print(G)

    idx = -1
    longest_mr = 0
    for i in range(n):
        if longest_mr < F[i]+G[i]-1:
            longest_mr = F[i]+G[i]-1
            idx = i

    sol = []

    def get_sol(F, X, idx, P):
        nonlocal sol
        sol.append(X[idx])
        if P[idx] != -1:
            get_sol(F, X, P[idx], P)

    if idx == n-1:
        get_sol(F, X, idx, F_parent)
        sol.reverse()
        return sol
    elif idx == 0:
        get_sol(F, X, idx, G_parent)
        return sol

    get_sol(F, X, idx, F_parent)
    sol.reverse()
    get_sol(G, X, G_parent[idx], G_parent)

    return sol


X = [4, 10, 5, 1, 5, 2, 3, 4]
# X = [1, 3, 2, 1]
X = [2, 5, 3, 2, 1, 23, 5, 7, 8, 5, 4, 3, 21, 2, 3, 4, 5, 7, 3]
# mr(X)


runtests(mr)
