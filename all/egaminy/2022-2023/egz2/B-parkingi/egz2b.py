# Marek Małek, 414880

# Rozwiązanie dynamiczne.

# Funkcja realizująca zadanie to: f(i,j)=min(f(i-1,p)+abs(X[i]-Y[j])), gdzie p: 0<=p<j
# Czyli jest to minimum z wzięcia j-tego parkingu (tutaj wartosc bezwgledna na odlegosc miedzy biurowcem a parkinkgiem)
# i dodajemy do tego minimalna wartosc, ktora mozemy otzrymac rozwazajac i-1 biurowcow zapewniajac dla i-1 biurowca p-ty parking
# gdzie p jest z zakresu od 0 do j, bo wynika z warunkow zadania, ze nie mozemy rozwazac wiekszego przedzialu w prawo, dlatego ze
# musza byc zachowane zasady bezpiecznego ruchu.

# Odczytanie wyniku to minimum z f(n-1,p), gdzie p jest z przedzialu [0,m-1], czyli to co otrzymamy dajac p-ty
# parking ostatniu biurowcowi i schodzac w dol rekurencyjnie.


# Zlozonosc czasowa: O(nm^2)

from egz2btesty import runtests


def parking(X, Y):
    # tu prosze wpisac wlasna implementacje
    from math import inf
    X.append(0)
    Y.append(0)
    n = len(X)
    m = len(Y)
    F = [[-1 for _ in range(m)] for _ in range(n)]

    def f(F, X, Y, i, j):
        if F[i][j] != -1:
            return F[i][j]

        if j < i:
            F[i][j] = inf
            return F[i][j]

        if i == 0:
            F[i][j] = abs(X[0]-Y[j])
            return F[i][j]

        res = inf
        for p in range(j):
            res = min(res, f(F, X, Y, i-1, p)+abs(X[i]-Y[j]))

        F[i][j] = res

        return res

    return f(F, X, Y, n-1, m-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)
