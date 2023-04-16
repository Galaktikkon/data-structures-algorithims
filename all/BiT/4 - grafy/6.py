# Rozmiary poddrzew
# Dostajemy na wejściu listę krawędzi drzewa (niekoniecznie binarnego!) oraz wyróżniony wierzchołek - korzeń.
# Każdy wierzchołek tworzy swoje własne poddrzewo. Dla każdego wierzchołka, wyznacz ilość wierzchołków w jego poddrzewie.

T=[[1,2],[0,3,4],[0,5,6],[1,7,8],[1],[2,9],[2,10,11,12],[3],[3],[5],[6],[6,13,14,15,16],[6],[11],[11],[11],[11]]

def subTrees(T):
    
    n=len(T)
    
    visited=[False for _ in range(n)]
    subSums=[0 for _ in range(n)]

    def treeVisit(G,i):
        nonlocal visited,subSums
        visited[i]=True
        for v in G[i]:
            if not visited[v]:
                subSums[i]+=1+treeVisit(G,v)+subSums[v]
        return 0
        
    
    treeVisit(T,0)
    
    return subSums

print(subTrees(T))