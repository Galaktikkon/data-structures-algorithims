# Marek Małek, 414880
# Algorytm opiera się na wielokrotnym użyciu algorytmu dijkstry. Na początku używamy zwykłej wersji, żeby wyznaczyć najkrotsze
# sciezki do zamków. Następnie z każdego zamku używamy go ponownie, ale z założeniem, że okradamy ten zamek oraz uwzględnieniem
# podwojonego kosztu za drogi i kosztu łapówki, aby przedostać się do innych zamków. W ten sposób

# szacowana złożonosć obliczeniowa: O(ElogV+VElogV) = O(VElogV)


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


def steal_Dijkstra(G, s, p, r, g, t):
    n = len(G)
    Q = PriorityQueue()
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = p
    Q.put((d[s], s))

    while not Q.empty():
        w, u = Q.get()
        if w == d[u]:
            for v, c in G[u]:
                if steal_relax(parent, d, v, u, c, r):
                    Q.put((d[v], v))
    for i in range(n):
        d[i] -= g
    return d[t]


def gold(G, V, s, t, r):
    # tu prosze wpisac wlasna implementacje
    paths = Dijkstra(G, s)
    n = len(paths)
    stolen = []
    for i in range(1, n):
        stolen.append(steal_Dijkstra(G, i, paths[i], r, V[i], t))
    return min(stolen)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
