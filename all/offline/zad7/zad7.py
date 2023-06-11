# Marek Małek, 414880
# Rozwiązanie dynamiczne. Algorytm działa na zasadzie znalezienia najdłuższej ścieżki poprzez uzupełnianie najdłuższych ścieżek do
# komnat po kolei biorąc kolumny - korzystamy z założenia, że możemy iść tylko w prawo, a nie w lewo, więc nigdy nie będziemy modyfikować
# wartości z lewej strony. Mamy więc jedną pętle po kolumnach i dwie, które rozważają ścieżki z dołu i z góry.
# Po wybraniu najoptymalniejszych, aktualizujemy tablicę, aby w opraciu o poprawną kolumnę obliczać następną.

# Szacowana złożoność obliczeniowa - O(n^2)

# Szacowana złożoność pamięciowa - O(n^2)

from zad7testy import runtests


def maze(L):
    from math import inf
    # tu prosze wpisac wlasna implementacje
    n = len(L)
    F = [[[-inf, -inf] for _ in range(n)] for _ in range(n)]
    # warunki początkowe
    F[0][0][0] = 0
    F[0][0][1] = 0
    # out = [[-inf for _ in range(n)] for _ in range(n)]
    i = 1
    while i < n and L[i][0] != "#":
        F[i][0][0] = F[i-1][0][0] + 1
        F[i][0][1] = F[i-1][0][1] + 1
        i += 1

    # realizacja funkcji
    for j in range(1, n):

        for i in range(n):
            if L[i][j] != "#":
                if i == 0:
                    F[i][j][0] = max(F[i][j-1][0]+1, F[i][j][0])
                else:
                    F[i][j][0] = max(F[i][j-1][0], F[i-1][j][0]) + 1

        for u in range(n-1, -1, -1):
            if L[u][j] != "#":
                if u == n-1:
                    F[u][j][1] = max(F[u][j-1][1]+1, F[u][j][1])
                else:
                    F[u][j][1] = max(F[u][j-1][1], F[u+1][j][1]) + 1

        for p in range(n):
            if F[p][j][0] > F[p][j][1]:
                # out[p][j] = F[p][j][0]
                F[p][j][1] = F[p][j][0]
            else:
                # out[p][j] = F[p][j][1]
                F[p][j][0] = F[p][j][1]

    return F[n-1][n-1][0] if F[n-1][n-1][0] > 0 else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
