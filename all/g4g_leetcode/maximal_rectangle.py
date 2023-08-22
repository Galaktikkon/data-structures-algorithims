def maximalRectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])
    F = [[0 for _ in range(m)] for _ in range(n)]
    F[0][0] = int(matrix[0][0])
    for i in range(1, n):
        if matrix[i][0] == "1":
            F[i][0] += 1
            if matrix[i-1][0] == "1":
                F[i][0] += F[i-1][0]
    for j in range(1, m):
        if matrix[0][j] == "1":
            F[0][j] += 1
            if matrix[0][j-1] == "1":
                F[0][j] += F[0][j-1]

    for i in F:
        print(i)


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

maximalRectangle(matrix)
