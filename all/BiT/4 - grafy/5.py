# Dany jest sejf, który odblokowuje się czterocyfrowym Pinem (0000-9999).
# Pod wyświetlaczem znajduje się kilka przycisków z liczbami od 1 do 9999 - przykładowo (13, 223, 782, 3902).
# Sejf ten działa inaczej niż normalny, wciśnięcie przycisku z liczbą powoduje dodanie liczby z przycisku do liczby na wyświetlaczu.
# Jeżeli suma jest większa niż 9999, to pierwsza cyfra zosaje obcięta.

# Jest tobie znany PIN oraz cyfry, które są aktualnei wyświetlane. Znajdź najkrótszą sekwencję naciśnięć przycisków,
# która pozwoli ci odblokować sejf. Jeżeli taka sekwencja nie istnieje, zwróc None.

from collections import deque

def safe(T,p,s):
    Q=deque()
    n=10000
    visited=[False  for _ in range(n)]
    visited[s]=True
    parent=[None for _ in range(n)]
    parent[s]=None
    d=[0 for _ in range(n)]
    d[s]=0
    entries=[]
    Q.appendleft(s)
    while Q:
        u=Q.pop()
        for v in T:
            if u==p:
                while u>0:
                    entries.append(parent[u])
                    u-=parent[u]
                entries.reverse()
                return entries
            if visited[(v+u)%n]==False:
                visited[(v+u)%n]=True
                d[(u+v)%n]=d[u]+1
                parent[(v+u)%n]=v
                Q.appendleft((v+u)%n)
                
    return None


T=[13,14]

print(safe(T,40,0))