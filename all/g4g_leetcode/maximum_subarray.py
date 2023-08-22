def maxSubArray(nums):
    n = len(nums)
    all_sum = 0
    plus_sum = 0
    sol = 0
    for i in range(n):
        tmp_sum = plus_sum
        all_sum += nums[i]
        plus_sum += nums[i]
        if all_sum < 0:
            all_sum = 0
        if nums[i] < 0:
            plus_sum = 0
        sol = max(sol, all_sum, tmp_sum)
    return sol


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [1]
nums = [5, 4, -1, 7, 8]
nums = [-1]
nums = [-1, -2]
maxSubArray(nums)
