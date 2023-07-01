def perfectSum(arr, n, psum):

    F = [-1 for _ in range(psum+1)]
    F[0] = 0

    def rec_sum(arr, n, psum, F, p):
        res = 0

        if psum == 0:
            return 1

        if F[psum] != -1:
            return F[psum]

        for i in range(p, n):
            if arr[i] <= psum:
                sub_res = rec_sum(arr, n, psum-arr[i], F, i)
                if sub_res != 0:
                    res += sub_res

        F[psum] = res

        return res

    rec_sum(arr, n, psum, F, 0)
    return F


psum = 10
arr = [2, 3, 5, 6, 8, 10]
n = len(arr)


def check(arr, n, psum):
    F = perfectSum(arr, n, psum)
    print(F)


check(arr, n, psum)
