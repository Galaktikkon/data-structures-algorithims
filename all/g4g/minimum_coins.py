
def bin_search(M, val):
    n = len(M)
    l = 0
    r = n-1
    mid = (l+r)//2
    while l < r:
        if M[mid] == val:
            return mid
        elif M[mid] < val:
            l = mid+1
        else:
            r = mid-1
        mid = (r+l)//2
    return mid


def minPartition(N):
    M = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    m = bin_search(M, N)
    val = N
    sol = []
    while m >= 0:
        while val-M[m] >= 0:
            val -= M[m]
            sol.append(M[m])
        m -= 1
    return sol


print(minPartition(41))
