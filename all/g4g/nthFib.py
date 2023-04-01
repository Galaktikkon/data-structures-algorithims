def nthFibonacci(n):
    f1=1
    f2=1
    for i in range(n-2):
        f1,f2=f2,f1+f2
    return f2%1000000007

print(nthFibonacci(3))