from collections import deque

# Dany jest ciag przedziałów postaci [a_i, b_i]. Dwa przedziały można skleić, jeśli mają dokładnie jeden punkt wspólny.
# Podaj algorytm, który sprawdza, czy da się uzyskać przedział [a,b] poprzez sklejenie odcinków.

T=[[8,10],[1,9],[1,3],[1,7],[3,6],[7,8]]

def DFS(G,a,b):
    
    n=len(G)
    visited=[False for _ in range(n)]
    
    def DFSVisit(G,i):
        visited[i]=True
        for v in G[i]:
            if not visited[v]:
                DFSVisit(G,v)
    
    DFSVisit(G,a)
            
    return visited[b]


def section(T,a,b):
    m=-1
    for i in T: m=max(m,i[1])
    G=[[] for _ in range(m+1)]
    for i in T: G[i[0]].append(i[1])
    return DFS(G,a,b)
    
print(section(T,1,6))