def nCr(n, r):
    # code here
    def factorial(n):
        res = 1
        for i in range(2, n+1):
            res *= i
        return res
    result = (factorial(n)//(factorial(r)*factorial(n-r))) % ((pow(10, 9))+7)
    return result if n >= r else 0


print(nCr(15, 3))
