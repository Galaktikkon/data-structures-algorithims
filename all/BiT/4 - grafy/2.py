# Wiadomość - Otrzymujemy na wejściu listę par ludzi, które się wzajemnie znają. Osoby są reprezentowane przez liczby od 0 do n-1.

# Dnia pierwszego osoba 0 przekazuje wiadomość wszystkim swoim znajomym. Dnia drugiego każdy ze znajomych 
# przekazuje tę wiadomść wszystkim swoim znajomym, którzy jej jescze nie znali itd.

# Napisz algorytm, który zwróci dzień, w którym najwięcej osób poznało wiadomość oraz ilość osób, które tego dnia ja otrzymały.


from collections import deque

def message(G,s):
    
    mess,day=0,0
    Q=deque()
    n=len(G)
    d=[0 for _ in range(n)]
    visited=[False for _ in range(n)]
    visited[s]=True
    Q.append((s,day))
    
    
    while Q:
        u,w=Q.pop()
        d[w]+=1 # tablica, ktora dla danego dnia przechowuje ile zostalo rozeslanych wiadomosci
        if d[w]>mess: # jezeli pewnego dnia rozeslano wiecej niz aktualnie jest najwiecej to podmiana wszystkiego
            mess=d[w]
            day=w
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                Q.append((v,w+1)) 
                # dorzuca sie do kolejki sasiada rozwazanego wierzcholka, z dniem o 1 wiekszym, 
                # bo dopiero nastepnego dnia sie go sprawdzi
        

    return day,mess

G=[[1,3],[0,3,5],[3,6,7],[0,1,2,4],[3],[1],[2],[8,9],[7],[7]]
H=[[1,3],[0,3],[3],[0,1,2]]

print(message(G,0))
print(message(H,0))