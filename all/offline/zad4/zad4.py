# Marek Małek, 414880
# Algorytm opiera się na wyszukaniu BFS'em najkrótszej scieżki, do czego sluży funkcja BFSPath, która zwraca tę ścieżkę.
# Następnie rozważamy czy po usunięciu jakiejś krawędzi z tej sekwencji (tj. najkrótszej ścieżki) powstanie inna ścieżka, 
# która będzie dluższa. Wiemy, że w najgorszym przypadku, w nowym grafie (czyli bez aktualnie rozważanej krawędzi) 
# długość najkrótszej ścieżki będzie taka sama jak w grafie jak w grafie pierwotnym. W głównej funkcji rozważane są możliwości:
# 1. rozważamy sytuację opisaną powyżej (usunięcie jednej krawędzi -> sprawdzenie czy ścieżka się wydłużyła)
# 2. w innym przypadku zwracamy None, tj. kiedy nie istnieje ścieżka w grafie pierwotnym - wtedy pętla while się nie wykona 
# lub kiedy nie uda się znaleźć dłuższej ścieżki.

# uwaga! usunięcie krawędzi jest realizowane przez nierozważanie w funkcji BFSPath połączenia p-q, gdzie p,q to krawędź usuwana.

# Szacowana złożoność: O(k*(V+E)), gdzie 'k' to dlugość najktrótszej ścieżki.

from zad4testy import runtests
from collections import deque

def BFSPath(G,s,t,p,q):
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
                if u==p:
                    if v!=q:
                        parent[v]=u
                        visited[v]=True
                        d[v]=d[u]+1
                        Q.append(v)
                else:
                    parent[v]=u
                    visited[v]=True
                    d[v]=d[u]+1
                    Q.append(v)
    return path

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    path=BFSPath(G,s,t,-1,-1)
    length=len(path)-1
    i,j=0,1
    while j<=length:
        poss=len(BFSPath(G,s,t,path[j],path[i]))
        if poss-1>length or poss==0:
            return path[i],path[j]
        j+=1
        i+=1
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )