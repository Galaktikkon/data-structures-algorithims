# Marek Małek, 414880
# Algorytm opiera się na wyszukaniu BFS'em najkrótszej scieżki, do tego sluży funkcja BFSPath, która zwraca tę ścieżkę.
# Następnie rozważamy czy po usunięciu jakiejś krawędzi z tej sekwencji (tj. najkrótszej ścieżki) powstanie inna ścieżka, 
# która będzie dluższa. Wiemy, że w najgorszym przypadku, w nowym grafie (czyli bez aktualnie rozważanej krawędzi) 
# długość najkrótszej ścieżki będzie taka sama jak w grafie jak w grafie pierwotnym. W głównej funkcji rozważane są możliwości:
# 1. jeśli nie istnieje ścieżka w grafie pierwotnym (czyli długość listy wierzchołków jest równa 0), to zwracamy None
# 2. jeśli lista składa się z dwu wierzchołków, to znaczy, że istnieje tylko jedna krawędź, którą można usunąć
# 3. w innym przypadku rozważamy sytuację opisaną powyżej (usunięcie jednej krawędzi -> sprawdzenie czy ścieżka się wydłużyła)

# Szacowana złożoność: O(k*(V+E)), gdzie 'k' to dlugość najktrótszej ścieżki

from zad4testy import runtests
from collections import deque

def BFSPath(G,s,t):
    Q=deque()
    n=len(G)
    visited=[False for _ in range(n)]
    parent=[None for _ in range(n)]
    d=[-1 for _ in range(n)]
    d[s]=0
    path=[]
    Q.append(s)
    while Q:
        u=Q.popleft()
        if u==t:
            while u!=s:
                path.append(u)
                u=parent[u]
            path.append(s)
            return path
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                visited[v]=True
                d[v]=d[u]+1
                Q.append(v)
    return path

def deleteEdge(G,p,q):
    G[p].remove(q)
    G[q].remove(p)
    return G

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    path=BFSPath(G,s,t)
    print(path)
    lenght=len(path)-1
    if not lenght:
        return None
    if lenght==2:
        return path[1],path[0]
    i,j=0,1
    while j<=lenght:
        H=G
        poss=len(BFSPath(deleteEdge(H,path[i],path[j]),s,t))
        if poss-1>lenght or poss==0:
            return path[i],path[j]
        j+=1
        i+=1
        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )