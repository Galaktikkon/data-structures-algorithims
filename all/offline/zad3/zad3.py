# Marek Małek, 414880

from zad3testy import runtests

def partition(A,p,r):
    
    x=len(A[r]) 
           
    i=p-1 
    
    for j in range(p,r): 
        if len(A[j])<=x:
            i+=1 
            A[j],A[i]=A[i],A[j] 
    A[r],A[i+1]=A[i+1],A[r]
    
    return i+1 

def quickSort(A,p,r):
    while p<r:
       q=partition(A,p,r)
       quickSort(A,p,q-1) 
       p=q+1   

def convert(A,index):
    return ord(A[index])-ord('a')

def reverseStrings(T):
    
    n=len(T)
    for i in range(n):
        if T[i]>T[i][::-1]:
            T[i]=T[i][::-1]
    
    return T

# def extend(T):
    
    n=len(T)
    
    maxLen=-float('inf')
    for i in T:
        maxLen=max(maxLen,len(i))
        
    for i in range(n):
        if len(T[i])<maxLen:
            while len(T[i])<maxLen:
                T[i]=chr(96)+T[i]
    
    return T

def countingSortString(A,index):
    
    n=len(A)
    
    C=[0]*26
    B=[0]*n
    
    for i in range(n):
        C[convert(A[i],index)]+=1
        
    for i in range(1,26):
        C[i]=C[i]+C[i-1]
        
    for i in range(n-1,-1,-1):
        B[C[convert(A[i],index)]-1]=A[i]
        C[convert(A[i],index)]-=1
        
    return B

def radixSort(T):
    
    k=len(T[0])
    for i in range(k-1,-1,-1):
        T=countingSortString(T,i)

    return T

def divArray(T):
    
    output=[]
    n=len(T)
    i,j=0,0
    while i<n:
        while i<n-1 and len(T[i])==len(T[i+1]):
            i+=1
        output.append(T[j:i+1])
        i+=1
        j=i
    return output

def sortAndMerge(T):
    
    output=[]
    for chunk in T:
        chunk=radixSort(chunk)
        output+=chunk
    
    return output

def strong_string(T):
    n=len(T)
    reverseStrings(T)
    quickSort(T,0,n-1)
    T=divArray(T)
    T=sortAndMerge(T)
    
    currMax,MaxLen=1,1

    i=1
    while i<n:
        while i<n and T[i]==T[i-1]:
            currMax+=1
            i+=1
        MaxLen=max(currMax,MaxLen)
        currMax=1
        i+=1
    return MaxLen

# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
