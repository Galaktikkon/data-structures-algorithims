def Dijkstra(G,s):
    from math import inf
    from queue import PriorityQueue
    n=len(G)
    Q=PriorityQueue()
    parent=[None for _ in range(n)]
    d=[inf for _ in range(n)]
    d[s]=0
    Q.put((d[s],s))
    
    while not Q.empty():
        w,u=Q.get()
        if w==d[u]:
            d[u]=w
            for v,c in G[u]:
                if relax(parent,d,v,u,c):
                    Q.put((d[v],v))
    return parent, d

def relax(parent,d,v,u,c):
    if d[v]>d[u]+c:
        d[v]=d[u]+c
        parent[u]=v
        return True
    return False

# G=[[(1,3),(3,7),(4,8)],[(3,4),(2,1)],[],[(2,2)],[(3,3)]]

# print(Dijkstra(G,0))

# def Dijkstra(G,s):S
    def relax(G,d,v,u,c):
        if d[v[0]][v[1]]>d[u[0]][u[1]]+c:
            d[v[0]][v[1]]=d[u[0]][u[1]]+c
            return True
        return False            
    n=len(G)
    from math import inf
    from queue import PriorityQueue
    d=[[inf for _ in range(n)] for _ in range(n)]
    Q=PriorityQueue()
    d[s[0]][s[1]]=G[s[0]][s[1]]
    Q.put((d[s[0]][s[1]],s))
    
    while not Q.empty():
        w,u=Q.get()
        if w==d[u[0]][u[1]]:
            d[u[0]][u[1]]=w
            for i,j in [(0,-1),(0,1),(-1,0),(1,0)]:
                if 0<=u[0]+i<n and 0<=u[1]+j<n:
                    if relax(G,d,(u[0]+i,u[1]+j),u,G[u[0]+i][u[1]+j]):
                        Q.put((d[u[0]+i][u[1]+j],(u[0]+i,u[1]+j)))
                        
    return d
                        
grid=[
    [9,4,9,9],
    [6,7,6,4],
    [8,3,3,7],
    [7,4,9,10]
]

costs=Dijkstra(grid,(0,0))
print(costs[len(grid)-1][len(grid)-1])
for i in costs: print(i)
    
    