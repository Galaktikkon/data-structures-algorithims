from random import randint
from collections import deque

# Dana jest dwuwymiarowa tablica N x N, w której każda komórka ma wartość "W" - reprezentującą wodę lub "L" - ląd.
# Grupę komórek wody połączyonych ze sobą brzegami nazywamy jeziorem.
# a) Policz, ile jest jezior w tablicy
# b) Policz, ile komórek zawiera największe jezioro
# c) Zakładając, że pola o indeksach [0][0] i [n-1][n-1] są lądem, 
#    sprawdź czy da się przejść drogą lądową z pola [0][0] do pola [n-1][n-1]. Można chodzić tylko na boki, nie na ukos.
# d) Znajdź najkrótszą ścieżkę między tymi punktami, wypisz po kolei indeksy pól w tej ścieżce.

def createLakes(n):
    
    M=[["L" if randint(0,3) else "W" for _ in range(n)] for _ in range(n)]
    M[0][0]=M[n-1][n-1]="L"
    for i in M: print(i)
    return M

def lakes(T):
    
    n=len(T)
    visited=[[False for _ in range(n)] for _ in range(n)]
    lakeCount=0
    maxLake,currMax=0,0
    
    def DFSVisit(G,i,j):
        nonlocal visited,maxLake,currMax
        currMax+=1
        visited[i][j]=True
        for (v,w) in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=v+i<n and 0<=w+j<n: 
                if not visited[i+v][j+w] and G[i+v][j+w]=="W":
                    DFSVisit(G,i+v,j+w)
                
        maxLake=max(maxLake,currMax)
        
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and T[i][j]=="W":
                lakeCount+=1
                currMax=0
                DFSVisit(T,i,j)
            
    return lakeCount,maxLake

def lakePaths(T):
        
    n=len(T)
    visited=[[False for _ in range(n)] for _ in range(n)]
    
    def DFSVisit(G,i,j,n):
        if i==j==n-1:
            return True
        nonlocal visited
        visited[i][j]=True
        for (v,w) in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=v+i<n and 0<=w+j<n: 
                if not visited[i+v][j+w] and G[i+v][j+w]=="L":
                    if DFSVisit(G,i+v,j+w,n):
                        return True
        return False
                    
    return DFSVisit(T,0,0,n)

def shortestPath(T):
    Q=deque()
    n=len(T)
    d=[[0 for _ in range(n)] for _ in range(n)]
    visited=[[False for _ in range(n)] for _ in range(n)]
    visited[0][0]=True
    parent=[[None for _ in range(n)] for _ in range(n)]
    Q.append((0,0))
    path=[(n-1,n-1)]
    pathSign=0
    while Q:
        i,j=Q.popleft()
        for v,w in [(0,1),(1,0),(0,-1),(-1,0)]:
            if 0<=i+v<n and 0<=j+w<n:
                if visited[i+v][j+w]==False and T[i+v][j+w]=="L":
                    parent[i+v][j+w]=(i,j)
                    visited[i+v][j+w]=True
                    d[i+v][j+w]=d[i][j]+1
                    if i+v==j+w==n-1:
                        path.append((i,j))
                        while j!=0 or i!=0:
                            path.append(parent[i][j])
                            i,j=parent[i][j]
                        path.reverse()
                        return path
                    Q.append((i+v,j+w))

    return False


print(lakes(createLakes(7)))
print(lakePaths(createLakes(7)))
print(shortestPath(createLakes(7)))
