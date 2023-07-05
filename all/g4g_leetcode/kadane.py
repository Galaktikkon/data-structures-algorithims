def maxSubArrSum(arr, n):
    if max(arr) < 0:
        return max(arr)
    plus_sum = 0
    all_sum = 0
    res = 0
    for i in range(n):
        tmp = plus_sum
        all_sum += arr[i]
        plus_sum += arr[i]
        if arr[i] < 0:
            plus_sum = 0
        if all_sum < 0:
            all_sum = 0
        res = max(res, tmp, all_sum)
    return res


arr = [1, 2, 3, -2, 5]
# arr = [-1, -2, -3, -4]
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)


def check(arr, n):
    print(arr)
    print("max possible sub-sum: ", maxSubArrSum(arr, n))


check(arr, n)
