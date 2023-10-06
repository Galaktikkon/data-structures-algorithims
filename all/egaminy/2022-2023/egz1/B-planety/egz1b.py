# Marek Małek

# Podejście dynamiczne.

# Warunek bazowy:
# koszt jaki musimy poniesc za b jednostek paliwa na planecie A (czyli i=0),
# to oczywiscie po prostu koszt tankowania b jednostek paliwa za cenę paliwa na startowej planecie (czyli b*C[0]).

# Sytuacja ogólna dla i-tej planety:
# Będąc na i-tej planecie koszt posiadania b jednostek paliwa, to jest minimum z dotankowania do b jednostek paliwa albo
# podroz z poprzedniej planety gdzie posiadalismy b+D[i]-D[i-1] jednostek paliwa (czyli mielsimy nadwyzke b ton paliwa nad
# kosztem dotarcia do i-tej planety z poprzedniej planety). Warto zwrócić uwagę, że tak naprawdę f(i,b) to minimalny koszt jaki
# nalezy poniesc bedąc przy i-tej planecie z b tonami paliwa - w ten sposób łatwiej zrozumieć dlaczego możemy się odwoływać tylko
# do poprzedniej planety, a nie sprawdzać możliwe koszty za b+D[i]-D[j] paliwa przy poprzednich planetach, gdzie są one
# z zakresu j: (0<=j<i). W ten sposób po prostu patrzymy jaki jest koszt b ton paliwa przy i-1-planecie i obliczamy koszt jaki nalezy
# poniesc przelatujac dystans miedzy i-1 planeta a i-ta (D[i]-D[i-1]).

# Ostatni przypadek, to ten kiedy nie mamy paliwa przy i-tej planecie:
# W tym wypadku dodatkowo rozwazamy uzycie teleportu i aktualizujemy koszt posiadania 0 ton paliwa przy planecie p,
# do ktorej moze nas zaprowadzic teleport.

# Wynikiem jest koszt jaki poniesiemy będąc przy n-1 planecie (planeta B), jednocześnie posiadając 0 ton paliwa. (F[n-1][0])

# Złożoność czasowa: O(nE)


from egz1btesty import runtests
from math import inf


def planets(D, C, T, E):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    F = [[inf for _ in range(E+1)] for _ in range(n)]

    for i in range(E+1):
        F[0][i] = C[0]*i

    for i in range(n):
        for b in range(E+1):
            if D[i]-D[i-1]+b <= E and i > 0:
                F[i][b] = min(F[i][b], F[i-1][D[i]-D[i-1]+b])
            if b > 0:
                F[i][b] = min(F[i][b-1]+C[i], F[i][b])
            if b == 0 and T[i][0] != i:
                F[T[i][0]][0] = min(F[T[i][0]][0], T[i][1]+F[i][0])

    return F[n-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
