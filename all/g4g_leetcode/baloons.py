def minCost(colors, neededTime):
    n = len(colors)
    i = 1
    keep_sum = 0
    while i <= n:
        to_keep = neededTime[i-1]
        while i < n and colors[i] == colors[i-1]:
            to_keep = max(to_keep, neededTime[i])
            i += 1
        keep_sum += to_keep  # type: ignore
        i += 1
    sol = sum(neededTime)-keep_sum
    print(sol)
    return sol


colors = "abaac"
neededTime = [1, 2, 3, 4, 5]

# colors = "abc"
# neededTime = [1, 2, 3]

# colors = "aabaa"
# neededTime = [1, 2, 3, 4, 1]

# colors = "aaabbbabbbb"
# neededTime = [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]

colors = "aaaaa"
neededTime = [1, 3, 4, 2, 3]
minCost(colors, neededTime)
