# Zaproponuj algorytm, który sprawdzi czy dany graf posiada cykl.

from collections import deque

def isCyclic(G,s):
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
            if visited[v] and parent[v]!=u and parent[v]!=None:
                return True
            if visited[v]==False:
                visited[v]=True
                d[v]=d[u]+1
                parent[v]=u
                Q.append(v)
                
    return False

G=[[1,2],[0,2],[0,1]]

# print(isCyclic(G,0))

def isCyclicDFS(G,s):
    
    def DFSVisit(G,i):
        nonlocal time, visited, parent,cyclic
        time+=1
        visited[i]=True
        for v in G[i]:
            if visited[v] and parent[v]!=i:
                cyclic=True
            if not visited[v]:
                parent[v]=i
                DFSVisit(G,v)
        time+=1
        
        
    n=len(G)
    visited=[False for _ in range(n)]
    visited[s]=True
    parent=[None for _ in range(n)]
    parent[s]=None
    cyclic=False
    time=0
    
    for i in range(n):
       if not visited[i]:
           DFSVisit(G,i)
           
    return cyclic

print(isCyclicDFS(G,0))