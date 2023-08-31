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

    return []


I = [[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
x = 1
y = 6
intuse(I, x, y)
# runtests(intuse)
