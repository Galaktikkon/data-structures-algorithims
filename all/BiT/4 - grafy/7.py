# Domy sklepy
# Mamy mapę miasteczka, w którym są domy i sklepy. 
# Na mapie sa również drogi (każda długości 1), które łączą dom z domem, albo dom ze sklepem.
# Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.

from random import randint
from collections import deque
def createCity(n):
    M=[["" for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if randint(0,4):
                M[i][j]="#"
            elif randint(0,2):
                M[i][j]="S"
            else:
                M[i][j]="D"
                
    for i in M: print(i)
    
    return M

# createCity(6)

def shops(M):
    n=len(M)
    Q=deque()
    visited=[[False for _ in range(n)] for _ in range(n)]
    d=[[-1 for _ in range(n)] for _ in range(n)]
    houses=[]
    for i in range(n):
        for j in range(n):
            if M[i][j]=="S":
                Q.append((i,j))
            elif M[i][j]=="D":
                houses.append([[i,j],0])
    
    while Q:
        i,j=Q.popleft()
        
        for v,w in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=i+v<n and 0<=j+w<n and M[i+v][j+w]!="S":
                if not visited[i+v][j+w]:
                    visited[i+v][j+w]=True
                    d[i+v][j+w]=d[i][j]+1
                    Q.append((i+v,j+w))
                    
    for house in houses:
        house[1]=d[house[0][0]][house[0][1]]
        
    return houses

print(shops(createCity(10)))