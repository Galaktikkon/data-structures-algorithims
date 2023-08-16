def goodDaysToRobBank(security, time):
    n = len(security)
    pref_left = [1 for _ in range(n)]
    pref_right = [1 for _ in range(n)]
    for i in range(1, n):
        pref_left[i] = pref_left[i-1]
        pref_right[n-i-1] = pref_right[n-i]
        if security[i] >= security[i-1]:
            pref_left[i] += 1
        if security[n-i] <= security[n-i-1]:
            pref_right[n-i-1] += 1
    sol = []
    for i in range(time, n-time):
        if pref_right[i-time]-pref_right[i] >= time <= pref_left[i+time]-pref_left[i]:
            sol.append(i)

    return sol


security = [5, 3, 3, 3, 5, 6, 2]
time = 2

# security = [1, 1, 1, 1, 1]
# time = 0

# security = [1, 2, 3, 4, 5, 6]
# time = 2

security = [1, 2, 3, 4]
time = 1

security = [4, 3, 2, 1]
time = 1

security = [1, 2, 5, 4, 1, 0, 2, 4, 5, 3, 1, 2, 4, 3, 2, 4, 8]
time = 2

print(goodDaysToRobBank(security, time))
