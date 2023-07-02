def minJumps(arr, n):
    # code here
    if not arr[0]:
        return -1
    if n < 2:
        return 0
    if arr[0] >= n-1:
        return 1
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):

        if i == n-1:
            return jumps

        if i + arr[i] >= n-1:
            return jumps+1

        max_reach = max(max_reach, arr[i]+i)

        steps -= 1

        if steps == 0:
            jumps += 1

            if max_reach <= i:
                return -1

            steps = max_reach-i

    return -1


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = [1, 4, 3, 2, 6, 7]
arr = [10, 4, 3, 2, 6, 7]
n = len(arr)


print(minJumps(arr, n))
