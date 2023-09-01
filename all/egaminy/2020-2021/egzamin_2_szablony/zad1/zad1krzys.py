from zad1testy import runtests
from collections import deque
from bisect import bisect_left


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

    return data, scaled_x, scaled_y


def intuse(I, x, y):
    I, x, y = scale(I, x, y)
    n = len(I)
    maxval = max(map(lambda t: max(t[0], t[1]), I))
    maxval = max(maxval, x, y)

    orgI = [x for x in I]

    def bfs(I, start):
        I.sort()

        first = list(map(lambda t: t[0], I))
        second = list(map(lambda t: t[1], I))

        available_from_start = [
            False for _ in range(maxval + 1)]  # type: ignore
        available_from_start[start] = True
        q = deque()
        q.append(start)
        while q:
            v = q.popleft()
            vpos = bisect_left(first, v)
            while vpos < n and first[vpos] == v:
                w = second[vpos]
                if not available_from_start[w]:
                    available_from_start[w] = True
                    q.append(w)
                vpos += 1

        return available_from_start

    fromx = bfs(I, x)

    I = list(map(lambda t: (t[1], t[0]), I))

    fromy = bfs(I, y)

    res = []
    i = 0
    for u, v in orgI:
        if fromx[u] and fromy[v]:
            res.append(i)
        i += 1

    return res


runtests(intuse)
