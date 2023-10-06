# Marek Małek
# Zauwazamy, ze aby obliczyc koszt jaki trzeba uiscic za dotarcie do potencjalnego zamku i dalszy przejazd od niego
# do zamku docelowego, mozemy uzyc dwoch wywolan Dijkstry. Pierwsze wywolanie z zamku s, aby otrzymac koszt normalnego przejscia
# do zamku okradanego oraz drugie z zamku t, ale juz z uwzglednieniem lapowek i podwojonego kosztu za ucieczke. W ten sposob mamy dwa
# kawalki drogi przechodzacej przez zamek ktory rabujemy, (w edgecaseach jest to uwzglednione tym, ze pierwsza Dijkstra zaklada,
# ze odlegosc do s z s to 0, a druga z t do t tez 0, wiec decydujac sie na rabowanie w ostatnim zamku czyli de facto porzucenie
# rabowania miedzy zamkami s i t, otrzymujemy poprawny wynik, tak samo w przypadku gdybysmy stwierdzili rabunek w zamku s i od razu
# bylibysmy scigani), kawali drogi laczymy i odejmujemy od nich koszt zysku jaki nam splynie z rabowania zamku, w ktorym owe sciezki
# sie lacza. W ten sposob dostajemy koszt za przejazd. Wybieramy z nich minimum.


# szacowana złożonosć obliczeniowa: O(ElogV+ElogV+n)=O(ElogV)


from egz1Atesty import runtests
from math import inf
from queue import PriorityQueue


def steal_relax(parent, d, v, u, c, r):
    if d[v] > d[u]+2*c+r:
        d[v] = d[u]+2*c+r
        parent[v] = u
        return True
    return False


def relax(parent, d, v, u, c):
    if d[v] > d[u]+c:
        d[v] = d[u]+c
        parent[v] = u
        return True
    return False


def Dijkstra(G, s):
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if relax(parent, d, v, u, c):
                    Q.put((d[v], v))
    return d


def steal_Dijkstra(G, s, r):
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    Q.put((d[s], s))
    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if steal_relax(parent, d, v, u, c, r):
                    Q.put((d[v], v))

    return d


def gold(G, V, s, t, r):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    paths = Dijkstra(G, s)
    stolen_paths = steal_Dijkstra(G, t, r)
    sol = inf
    for i in range(n):
        sol = min(sol, paths[i]+stolen_paths[i]-V[i])

    return sol


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
