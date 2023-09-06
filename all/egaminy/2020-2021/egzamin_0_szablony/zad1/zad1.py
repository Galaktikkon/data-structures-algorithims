from zad1testy import runtests


def counting_sort(A, k, idx):
    n = len(A)
    B = [0 for _ in range(n)]
    C = [0 for _ in range(k+1)]
    for i in range(n):
        C[ord(A[i][idx])-ord('a')] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[ord(A[i][idx])-ord('a')]-1] = A[i]
        C[ord(A[i][idx])-ord('a')] -= 1
    return B


def tanagram(x, y, t):
    if len(x) != len(y):
        return False
    n = len(x)
    x_arr = [(x[i], i) for i in range(n)]
    y_arr = [(y[i], i) for i in range(n)]

    x_arr = counting_sort(x_arr, 26, 0)
    y_arr = counting_sort(y_arr, 26, 0)

    for i in range(n):
        # type: ignore
        if x_arr[i][0] != y_arr[i][0] or abs(x_arr[i][1]-y_arr[i][1]) > t:
            return False

    return True


runtests(tanagram)
