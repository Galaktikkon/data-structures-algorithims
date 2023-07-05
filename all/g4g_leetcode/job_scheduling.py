def JobScheduling(jobs, n):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    sol = [0 for _ in range(n)]
    res = [0, 0]
    for i in range(n):
        j = jobs[i].deadline
        while j > 0:
            if sol[j-1] == 0:
                sol[j-1] = jobs[i].profit
                res[0] += 1
                res[1] += sol[j-1]
                break
            j -= 1

    return res


Jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
N = len(Jobs)


def check(Jobs, N):
    sol = JobScheduling(Jobs, N)
    print(sol)
    print("jobs done:", sol[0])
    print("profit made:", sol[1])


check(Jobs, N)
