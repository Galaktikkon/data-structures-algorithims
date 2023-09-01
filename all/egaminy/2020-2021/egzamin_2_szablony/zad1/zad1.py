from zad1testy import runtests


def scale(data, x, y):
    A = []
    for a, b in data:
        A.append(a)
        A.append(b)
    A.sort()
    dic = {}
    last = -1
    k = -1
    scaled_x, scaled_y = x, y

    for val in A:
        if val != last:
            k += 1
        if val == x:
            scaled_x = k
        elif val == y:
            scaled_y = k
        if val not in dic:
            dic[val] = k
        last = val

    for i, sec in enumerate(data):
        data[i] = (dic[sec[0]], dic[sec[1]])

    return scaled_x, scaled_y


def get_graph_x(I, a, b):
    G = [[] for _ in range(b-a+1)]

    for x, y in I:
        if x >= a and y <= b:
            G[x-a].append(y-a)
    return G


def get_graph_y(I, a, b):
    G = [[] for _ in range(b-a+1)]

    for x, y in I:
        if x >= a and y <= b:
            G[y-a].append(x-a)
    return G


def bfs(G, s, visited):
    visited[s] = True
    from collections import deque
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)

    return visited


def intuse(I, x, y):
    """tu prosze wpisac wlasna implementacje"""
    new_x, new_y = scale(I, x, y)
    G_x = get_graph_x(I, new_x, new_y)
    G_y = get_graph_y(I, new_x, new_y)
    n = len(G_x)

    x_visited = bfs(G_x, 0, [False for _ in range(n)])
    y_visited = bfs(G_y, new_y-new_x, [False for _ in range(n)])

    sol = []

    for i, sec in enumerate(I):
        a, b = sec
        if 0 <= a-new_x < n and 0 <= b-new_x < n:
            if x_visited[a-new_x] and y_visited[b-new_x]:
                sol.append(i)

    return sol


I = [(3000000, 4000000), (2000000, 5000000), (1000000, 3000000),
     (4000000, 6000000), (1000000, 4000000)]
x = 1000000
y = 6000000

runtests(intuse)
