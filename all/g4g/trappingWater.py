def trappingWater(arr, n):
    # Code here
    trappedWater = 0

    i = 0
    j = 0
    leftWall = arr[i]
    rightWall = arr[j]
    while True:

        while j < n-1 and leftWall <= arr[j]:
            j += 1
        rightWall = arr[j]
        while i < j:
            if min(leftWall, rightWall)-arr[i] > 0:
                trappedWater += min(leftWall, rightWall)-arr[i]
            i += 1

        leftWall = max(leftWall, arr[i])

        j += 1
        if j > n-1:
            break

    return trappedWater


A = [0, 9, 0, 0, 6, 1, 3, 8]

print(trappingWater(A, 8))
