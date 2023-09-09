# Marek Małek, 414880

# W algorytmie używam sortowania przez zliczanie, bo znany jest nam przedział danych i w ten sposób jest to sortowanie prawdziwie
# liniowe (=Theta(n+k), gdzie k=n, więc jest to Theta(2n)=Theta(n)). Sortuję punkty względem pierwszej zmiennej.
# W tablicy Y trzymam wartość tak jak we wskazówce czyli Y[i] to liczba punktów, których wspólrzędna y jest większa lub równa i.
# W tablicy X trzymam wartości takie, że: X[i] to liczba wystąpień liczby i w tablicy P, gdzie patrzę na pierwszą współrzędną, czyli
# ile jest takich x-ów w tablicy P.

# Finalnie przechodzę jeszcze raz po tablicy (już posortowanej) i obliczam ile dany punkt dominuje innych punktów:
# Jest to pozycja i w posortowanej tablicy (tablica posortowana oznaczona jest jako S, wtedy sortowanie daje nam potencjalną siłę punktu,
# ale musimy ją skorygować)
# z odjęciem liczby punktów o współrzędnej y większej od aktualnie rozważanej
# (+1 bo nie wliczamy aktualnie rozważanej krotki) oraz odjęcia liczby punktów o tej
# samej współrzędnej x (+1 tak analogicznie jak w poprzednim zdaniu). Po potencjalnym zmianie najsilniejszego punktu odejmuję liczbę
# wystąpień współrzędnej x w tablicy X, aby nie tworzył się błąd w sytuacji, kiedy jesteśmy na pierwszej krotce o współrzędnej x
# i chcemy odjąć ile ma tą samą współrzędną x (robi to za nas po prostu iterator pętli, więc musimy to korygować).

# Cały czas aktualizujemy wartość maksymalną w zmiennej sol.

# Złożoność czasowa  = O(n), jako, że korzystamy tylko z operacji linowych.
# Sortowanie przez zliczanie jest liniowe (wytłumaczenie wyżej)
# Budowanie tablic pomocniczych (X,Y) oraz szukanie rozwiązania to też są operacje linowe względem n.

from egz2atesty import runtests


def countingSort(A, k, idx):
    n = len(A)

    C = [0]*k
    B = [0]*n

    for i in range(n):
        C[A[i][idx]] += 1

    for i in range(1, k):
        C[i] = C[i]+C[i-1]

    for i in range(n-1, -1, -1):
        B[C[A[i][idx]]-1] = A[i]
        C[A[i][idx]] -= 1

    return B


def dominance(P):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    S = countingSort(P, n+1, 0)
    X = [0 for _ in range(n+1)]
    Y = [0 for _ in range(n+1)]

    for i in range(n):
        Y[P[i][1]] += 1
        X[P[i][0]] += 1

    for i in range(n-1, -1, -1):
        Y[i] = Y[i+1]+Y[i]

    sol = -1
    for i in range(n-1, -1, -1):
        sol = max(sol, i-Y[S[i][1]]+1-X[S[i][0]]+1)  # type: ignore
        X[S[i][0]] -= 1  # type: ignore
    return sol


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance, all_tests=True)
