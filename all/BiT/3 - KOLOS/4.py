import math
import random

def convert(A,a):
    
    n=len(A)
    for i in range(n):
        A[i]=(A[i],math.log(A[i],a))

def bubbleSort(A):
    n=len(A)
    for i in range(n):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

def bucketSort(A,key):
    n=len(A)
    norm=-float('inf')
    
    for i in range(n):
        norm=max(norm,A[i][key])
    
    buckets=[[] for _ in range(n)]
    
    for el in A:
        normEl=el[key]/norm
        bucketInd=int(n*normEl -1 if n*normEl>0 else 0)
        buckets[bucketInd].append(el)
        
    for bucket in buckets:
        bucket=bubbleSort(bucket)
        
    output=[]
    
    for bucket in buckets:
        output+=bucket
    
    return output

def fastSort(T,a):
    n=len(T)
    convert(T,a)
    # print(T)
    T=bucketSort(T,1)
    
    for i in range(n):
        T[i]=T[i][0]
        
    return T

T=[round((2**(random.uniform(0.000000001,1))),2) for _ in range(15)]

print(fastSort(T,2))



