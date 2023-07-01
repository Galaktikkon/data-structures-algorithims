def stockBuySell(A, n):
    # code here
    solutions = []
    i, j = 1, 0
    while i < n:
        if A[i-1] < A[i]:
            i += 1
        else:
            if i-j > 0:
                solutions.append((j, i-1))
            j = i
            i += 1
    if i == n:
        solutions.append((j, i-1))
    return solutions


A = [100, 180, 260, 310, 40, 535, 695]
n = 7

print(stockBuySell(A, n))
