def numberOfArithmeticSlices(nums):
    n = len(nums)
    F = [0 for _ in range(n)]
    ans = 0
    for i in range(2, n):
        if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
            F[i] = F[i-1]+1
            ans += F[i]
    return ans


nums = [1, 2, 3, 4]
nums = [1, 3, 5, 7, 9]
# nums = [1, 2, 3, 4, 5, 6]
# nums = [1, 2, 3, 8, 9, 10]
# nums = [1]
# nums = [2, 1, 3, 4, 2, 3]
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
numberOfArithmeticSlices(nums)
