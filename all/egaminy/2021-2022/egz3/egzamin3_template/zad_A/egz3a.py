from egz3atesty import runtests

T = 100
I = [(3, 10), (0, 5), (20, 30), (25, 35), (26, 26)]


def snow(T, I):
    # tu prosze wpisac wlasna implementacje
    A = []
    for i in range(len(I)):
        if I[i][0] == I[i][1]:
            A.append(I[i][0])
        else:
            A.append(I[i][0])
            A.append(I[i][1])
    A.sort()
    n = len(A)
    F = [0 for _ in range(n)]
    for i in range(len(I)):
        start = I[i][0]
        end = I[i][1]
        j = 0
        while j <= n and A[j] < start:
            j += 1
        while j < n and A[j] <= end:
            F[j] += 1
            j += 1
    return max(F)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
