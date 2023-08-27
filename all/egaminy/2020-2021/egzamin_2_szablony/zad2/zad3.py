from zad3testy import runtests


def lamps(n, T):
    """tu prosze wpisac wlasna implementacje"""
    max_blue = 0
    L = [0 for _ in range(n)]
    blue = 0
    for a, b in T:
        for i in range(a, b+1):
            if L[i] == 0:
                L[i] = 1
            elif L[i] == 1:
                L[i] = 2
                blue += 1
            elif L[i] == 2:
                L[i] = 0
                blue -= 1
        max_blue = max(max_blue, blue)

    return max_blue

runtests(lamps)
