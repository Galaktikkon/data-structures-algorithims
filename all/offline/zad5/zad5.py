from zad5testy import runtests

def Dijkstra(G,s,S):
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
        for v,c in G[u]:
            if relax(v,c,d,u):
                Q.put((G[v],v))
    return d

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    from math import inf
    G=[[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    for i in range(len(S)):
        for j in range(len(S)):
            if j!=i:
                G[S[i]].append((S[j],0))
    dist=Dijkstra(G,a,S)
    return dist[b] if dist[b]!=inf else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )