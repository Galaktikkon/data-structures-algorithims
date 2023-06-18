from zad8testy import runtests


def dfs(T):
    n = len(T)
    m = len(T[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    A = [0 for _ in range(m)]

    def dfs_visit(T, i, j):
        nonlocal visited, fuel
        visited[i][j] = True
        for u, v in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i+u < n and 0 <= j+v < m:
                if not visited[i+u][j+v] and T[i+u][j+v] > 0:
                    dfs_visit(T, i+u, j+v)
        fuel += T[i][j]

    for j in range(m):
        fuel = 0
        if T[0][j] > 0:
            if not visited[0][j]:
                dfs_visit(T, 0, j)
        A[j] = fuel

    return A


# T = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# T2 = [[6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# def printmap(T):
#     for i in T:
#         print(i)
#     print()
#     print(dfs(T))


# printmap(T)
# printmap(T2)


def plan(T):
    # tu prosze wpisac wlasna implementacje
    # print(T)
    from queue import PriorityQueue
    Q = PriorityQueue()
    A = dfs(T)
    m = len(T[0])
    counter = 1
    lenght = A[0]
    idx = 1
    while lenght < m-1:
        while idx <= lenght:
            if A[idx] > 0:
                Q.put(A[idx]*(-1))
            idx += 1
        lenght -= Q.get()
        counter += 1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
