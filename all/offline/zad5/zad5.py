from zad5testy import runtests

def Dijkstra(G,s):
    def relax(v,c,d,u):
        if d[v]>d[u]+c:
            d[v]=d[u]+c
            return True
        return False
    n=len(G)
    from math import inf
    from queue import PriorityQueue
    d=[inf for _ in range(n)]
    Q=PriorityQueue()
    d[s]=0
    Q.put((d[s],s))
    while not Q.empty():
        w,u=Q.get()
        if w>d[u]:
            continue
        for v,c in G[u]:
            if d[v]>d[u]+c:
                d[v]=d[u]+c
                Q.put((d[v],v))
    return d

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    from math import inf
    G=[[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    print(G)
    for i in range(len(S)):
        for j in range(len(S)):
            if j!=i:
                G[S[i]].append((S[j],0))
    
    dist=Dijkstra(G,a)
    return dist[b] if dist[b]!=inf else None

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( spacetravel, all_tests = False )

E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
print(spacetravel(7,E,S,1,5))