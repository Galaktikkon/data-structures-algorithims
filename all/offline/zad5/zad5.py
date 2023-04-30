from zad5testy import runtests
from math import inf
from queue import PriorityQueue

def Dijkstra(G,s,S,A):
    def relax(v,c,d,u):
        if d[v]>d[u]+c:
            d[v]=d[u]+c
            return True
        return False
    n=len(G)
    d=[inf for _ in range(n)]
    Q=PriorityQueue()
    d[s]=0
    Q.put((d[s],s))
    flag=False
    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            if not flag and A[u]:
                for v in S:
                    if relax(v,0,d,u):
                        Q.put((d[v],v))
                flag=True
            else:
                for v,c in G[u]:
                    if relax(v,c,d,u):
                        Q.put((d[v],v))
    return d

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje
    G=[[] for _ in range(n)]
    for i in range(len(E)):
        G[E[i][0]].append((E[i][1],E[i][2]))
        G[E[i][1]].append((E[i][0],E[i][2]))
    A=[False for _ in range(n)]
    for i in S: A[i]=True
    
    dist=Dijkstra(G,a,S,A)
    return dist[b] if dist[b]!=inf else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )