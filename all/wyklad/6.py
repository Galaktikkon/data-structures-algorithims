# ALGORYTMY GRAFOWE

# graf skierowany - para G = (V,E):
# V = {v1, ...,vn} - zbiór wierzchołków
# E = {e1, ...,en} - podbzbiór (V x V) / (ei,ei) - czyli (na ogół) bez pętli typu e1-e1

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
# ale jest to ok dla grafów gęstych, które mają blisko O(n^2) krawędzi

# 3. lista sąsiedztwa

# tablica
# |
# V
# 
# 1 -> 2
# 2 -> 4
# 3 
# 4 -> 1 -> 3

# sprawdzenie czy dana krawędź istnieje ma potencjalnie złożoność O(n)
# przegląd krawędzi wychodzących z danego wierzchołka V ma złożoność O(d(V)), gdzie d(V) - stopień wierzchołka,
# czyli liczba wychodzących krawędzi

# PRZEJŚCIE GRAFU W SZERZ - BFS (breadth-first search) - O(V+E) - reprezentacja listowa, O(V^2) - reprezentacja macierzowa

# -> znajduje najkrótsze ścieżki w sensie liczby krawędzi
# -> inne zastosowania: testowanie spójności grafu, testowanie dwudzielności
# -> wykrywanie cykli

def BFS(G,s):
    pass

# PRZEJŚCIE GRAFU W GŁĄB - DFS (depth-first search)

# -> testowanie spójności grafu, testowanie dwudzielności
# -> wykrywanie cykli
# -> sortowanie topologiczne
# -> silnie spójne składowe
# -> wyznaczanie cyklu euelera
# -> mosty i punkty artykulacji
# most to taka krawędź, której usunięcie rozspójnia graf
# punkt artykulacji, to wierzchołek, którego usunięcie zwiększa liczbę spójnych składowych grafu

def DFS(G,s):
    pass

# SORTOWANIE TOPOLOGICZNE





