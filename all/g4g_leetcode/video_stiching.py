def videoStitching(clips, time):
    from math import inf
    n = len(clips)
    F = [inf for _ in range(time+1)]
    F[0] = 0
    clips = sorted(clips, key=lambda x: x[1])
    clips = sorted(clips, key=lambda x: x[0])

    for i in range(n):
        s, t = clips[i]
        for j in range(s, t+1):
            if j <= time:
                F[j] = min(F[j], F[s]+1)
    print(clips)
    print(F, F[time] if F[time] != inf else -1)

    return F[time] if F[time] != inf else -1


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
time = 10

clips = [[0, 4], [2, 8]]
time = 5
videoStitching(clips, time)
