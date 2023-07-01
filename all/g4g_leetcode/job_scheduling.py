def JobScheduling(Jobs, n):
    Jobs.sort(key=lambda x: x[2], reverse=1)
    i = 0
    time = n
    profit = 0
    job_counter = 0
    while time >= Jobs[i][1]:
        time -= Jobs[i][1]
        profit += Jobs[i][2]
        job_counter += 1
        i += 1
    return [job_counter, profit]


Jobs = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
N = len(Jobs)


def check(Jobs, N):
    sol = JobScheduling(Jobs, N)
    print("jobs done:", sol[0])
    print("profit made:", sol[1])


check(Jobs, N)
