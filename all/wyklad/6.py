from collections import deque
# ALGORYTMY GRAFOWE

# graf skierowany - para G = (V,E):
# V = {v1, ..., vn} - zbiór wierzchołków
# E = {e1, ..., en} - podbzbiór (V x V) / (ei,ei) - czyli (na ogół) bez pętli typu e1-e1

# gref nieskierowany jest zdefiniowany analogicznie, ale każda krawędź to zbiór dwuelementowy.
#   -> na ogół reprezentowany jako graf skierowany z krawędziami w obie strony.

# często z krawędziami i wierzchołkami wiążemy dodatkowe informacje (np. wagi/długości - grafy ważone)

# REPREZENTACJE GRAFÓW

# 1. przez listę/tablicę krawędzi (najrzadziej używana)

# [4,3] -> [1,2] -> [2,4] -> [4,1] --[

# 2. macierzowa
#     1 2 3 4 
#   1 - T F F
#   2 F - F T   -> na podstawie macierzy: istnieją krawędzie np. 4-1, 4-2, 2-4, z def wyżej wynika, że przekątna jest pusta.
#   3 F F - F
#   4 T T F -

# testowanie czy istnieje krawędź ma złożoność O(1)
# przegląd krawędzi wychodzących z danego wierzchołka ma złożoność O(n) -  dla grafów rzadkich forsuje to O(n^2),
# ale jest to ok dla grafów gęstych, które mają blisko O(n^2) krawędzi, więc minus złożoności pamięciowej jest pomijalny

# 3. lista sąsiedztwa

# tablica, gdzie pod indeksem i-tego wierzchołka mamy tablicę jego sąsiadów (skierowań na)
# np. wierzchołek 4 ma skierowania na 1 i 3
# |
# V

# i
# 1 -> [2]
# 2 -> [4]
# 3 -> []
# 4 -> [1,3]

# sprawdzenie czy dana krawędź istnieje ma potencjalnie złożoność O(n)
# przegląd krawędzi wychodzących z danego wierzchołka V ma złożoność O(d(V)), gdzie d(V) - stopień wierzchołka,
# czyli liczba wychodzących krawędzi

# PRZEJŚCIE GRAFU W SZERZ - BFS (breadth-first search) - O(V+E) - reprezentacja listowa, O(V^2) - reprezentacja macierzowa

# -> znajduje najkrótsze ścieżki w sensie liczby krawędzi
# -> inne zastosowania: testowanie spójności grafu, testowanie dwudzielności
# -> wykrywanie cykli

def BFS(G,s):
    Q=deque()
    n=len(G)
    d=[-1 for _ in range(n)]
    d[s]=0
    visited=[False for _ in range(n)]
    visited[s]=True
    parent=[None for _ in range(n)]
    parent[s]=None
    Q.append(s)
    
    while Q:
        u=Q.popleft()
        for v in G[u]:
            if visited[v]==False:
                visited[v]=True
                d[v]=d[u]+1
                parent[v]=u
                Q.append(v)
                
    return d,visited,parent

G=[[2,3,4],[2,4,5],[0,1],[4,0,6],[0,1,3,5],[1,4],[3]]

print(BFS(G,0)[0])


# PRZEJŚCIE GRAFU W GŁĄB - DFS (depth-first search) - O(V+E) - reprezentacja listowa, O(V^2) - reprezentacja macierzowa

# -> testowanie spójności grafu, testowanie dwudzielności
# -> wykrywanie cykli
# -> sortowanie topologiczne
# -> silnie spójne składowe
# -> wyznaczanie cyklu euelera
# -> mosty i punkty artykulacji
# most to taka krawędź, której usunięcie rozspójnia graf
# punkt artykulacji, to wierzchołek, którego usunięcie zwiększa liczbę spójnych składowych grafu

def DFS(G,s):
    
    def DFSVisit(G,i):
        nonlocal time, visited, parent,topoList
        time+=1 # czas odwiedzenia wierzchołka i
        visited[i]=True
        for v in G[i]:
            if not visited[v]:
                parent[v]=i
                DFSVisit(G,v)
        time+=1 # czas przetworzenia i-tego wierzchołka
        topoList.append(chr(i+97))
        
        
    n=len(G)
    topoList=[]
    visited=[False for _ in range(n)]
    # visited[s]=True # off dla topoSort'a
    parent=[None for _ in range(n)]
    parent[s]=None
    
    time=0
    
    for i in range(n): #przeszukanie całego grafu, jeśli zechemy z jednego wierzchołka odpalić DFS to tylko z nirgo odpalamy!
       if not visited[i]:
           DFSVisit(G,i)
           
           
    return topoList
    
# SORTOWANIE TOPOLOGICZNE

# DAG - directed acyclic graph (skierowany graf acykliczy) - tylko dla takiego typu grafów

# Sortowanie topologiczne dagu: ułożenie jego wierzchołków w takiej kolejności, że krawędzie wskazują wyłącznie z lewej na prawą
# -> linearyzacja częściowego porządku: wyznaczenie kolejności realizacji zadań, w przypadku, w którym niektóre mają wyższy priorytet,
# czyli muszą być wykonane przed innymi, np. ubranie się (skarpetki zakładamy przed butami XD)

# Algorytm:
# - uruchomić DFS i po "przetworzeniu" każdego wierzchołka dopisać go na początek tworzonej listy

def TopologicalSort(G):
    # implementacja powyżej, po prostu zmodyfikowany DFS
    pass

Tasks=[[1,2],[2,4],[],[],[3,6],[4],[]]

print(DFS(Tasks,0))





