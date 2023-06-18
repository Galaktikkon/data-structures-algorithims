# Marek Małek, 414880

# Rozwiązanie zachłanne. Na początku przeprowadzamy konwersję danych, aby zredukować problem do jednej tablicy o rozmiarze m.
# Na każdym polu jest rozmiar wpisany rozmiar plamy (tj. ile ropy można z niej pozyskać). Jeśli plama zajmuje tez inne miejsce na drodze,
# to jej pojemność jest wstawiamy tylko w najwcześniejszym polu, które ma do niej dostep, zapobiega to wielokrotnemu pozyskiwaniu tej
# samej ropy objetości ropy z kilku miejsc, a de facto tej samej plamy. Do konwersji wykorzystujemy algorytm dfs (klasyczny problem z mapą
# i jeziorami). Podejscie zachlanne polega na wzięciu na początku ropy z pola, na którym stoimy (musimy je wziąć, żeby móc się poruszyć),
# a następnie bierzemy zawsze największą możliwą plamę w zasięgu (do tego wykorzystujemy kolejkę priorytetową), jeśli skończyło nam się
# paliwo, to chcemy wziąć kolejną największa plamę z tych, które już odwiedziliśmy.

# Szacowana złożoność obliczeniowa O(mlogm), gdzie m to dlugość ścieżki.

from zad8testy import runtests


def dfs(T):
    n = len(T)
    m = len(T[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    A = [0 for _ in range(m)]

    def dfs_visit(T, i, j):
        nonlocal visited, fuel
        visited[i][j] = True
        for u, v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i+u < n and 0 <= j+v < m:
                if not visited[i+u][j+v] and T[i+u][j+v] > 0:
                    dfs_visit(T, i+u, j+v)
        fuel += T[i][j]

    for j in range(m):
        fuel = 0
        if T[0][j] > 0:
            if not visited[0][j]:
                dfs_visit(T, 0, j)
        A[j] = fuel

    return A


def plan(T):
    # tu prosze wpisac wlasna implementacje
    # print(T)
    from queue import PriorityQueue
    Q = PriorityQueue()
    A = dfs(T)
    m = len(T[0])
    counter = 1
    lenght = A[0]
    idx = 1
    while lenght < m-1:
        while idx <= lenght:
            if A[idx] > 0:
                Q.put(A[idx]*(-1))
            idx += 1
        lenght -= Q.get()
        counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
