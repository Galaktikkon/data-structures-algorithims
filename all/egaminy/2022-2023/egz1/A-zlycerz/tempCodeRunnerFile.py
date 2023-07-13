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
    print(stolen)
    return min(stolen)


# gold(G, V, s, t, r)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)