from zad1testy import runtests

def get_graph(I, x, y):
    G = [[] for _ in range(y-x+1)]

    for a, b in I:
        if a >= x and b <= y:
            G[a-x].append(b-x)

    return G


def intuse(I, x, y):
    """tu prosze wpisac wlasna implementacje"""
    G = get_graph(I, x, y)
    sol = []
    n = len(G)
    visited = [False for _ in range(n)]
    idx = {}
    for i, sec in enumerate(I):
        if sec not in idx:
            idx[sec] = [[], False]
            idx[sec][0].append(i)
        else:
            idx[sec][0].append(i)

    def write_to_dic(path):
        nonlocal sol, idx
        i, j = 0, 1
        n = len(path)
        # print(path)
        while j < n:
            idx[(path[i], path[j])][1] = True
            i += 1
            j += 1

    def dfs(G, v, path, x, y):
        print(v)
        if v == y-x:
            write_to_dic(path+[v+x])
            return
    
        path.append(v+x)
        visited[v]=True
        
        for u in G[v]:
            if not visited[u]:
                dfs(G, u, path, x, y)
        
        path.pop()
        visited[v]=False

    dfs(G, 0, [], x, y)

    for i, flag in idx.values():
        if flag:
            sol += i

    # print(sol)

    return sol


I = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]
x = 1
y = 6


# intuse(I,x,y)

runtests(intuse)