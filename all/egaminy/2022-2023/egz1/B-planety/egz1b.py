# Marek Małek, 414880
# Podejście dynamiczne, ale nie udało się w implementacji. Funkcja f(i,b) jest funkcją minimum po opcjach lotu do planety i z nieokreśloną
# ilością paliwa i dotankowanie, aby mieć b oraz dojścia do planety pośredniej j, z której bierzemy teleport i tankujemy do b.
# Odczytanie rozwiązania to przejście po wszystkich możliwych wartościach paliwa, będąc na ostatniej planecie.

from egz1btesty import runtests
from math import inf

D = [0, 1, 4, 6, 7, 10, 11, 12, 13, 15, 16]
C = [2, 6, 2, 10, 2, 10, 4, 6, 8, 8, 4]
T = [(0, 0), (5, 8), (2, 0), (7, 10), (10, 6), (10, 26),
     (10, 6), (10, 2), (8, 0), (9, 0), (10, 2)]
E = 5

D = [0, 5, 10, 20]
C = [2, 1, 3, 9]
T = [(2, 3), (3, 7), (2, 10), (3, 10)]
E = 10


def planets(D, C, T, E):
    # tu prosze wpisac wlasna implementacje
    result = inf
    n = len(D)
    F = [[inf for _ in range(E+1)] for _ in range(n)]
    F[0][0] = 0
    for i in range(E+1):
        F[0][i] = C[0]*i
    for i in range(n):
        for b in range(E+1):
            for j in range(i):
                tp = inf
                if T[i][0] == i:
                    tp = T[i][1]
                to_fly = inf
                if D[i]+b < E+1:
                    to_fly = F[i-1][D[i]+b]
                else:
                    to_fly = F[i][b-1]+C[i]
                F[i][b] = min(to_fly+b*C[i], tp+F[j][b]+b*C[i])

    for i in F:
        print(i)

    # odczytanie rozwiazania
    for i in range(E+1):
        result = min(F[n-1][i], result)
    return result


print(planets(D, C, T, E))

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(planets, all_tests=False)
