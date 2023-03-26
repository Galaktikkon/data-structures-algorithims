# Marek Małek, 414880

from zad3testy import runtests

def convert(A,index):
    return ord(A[index])-ord('a')

def reverseStrings(T):
    
    n=len(T)
    for i in range(n):
        if T[i]>T[i][::-1]:
            T[i]=T[i][::-1]
    
    return T

def extend(T):
    
    n=len(T)
    
    maxLen=-float('inf')
    for i in T:
        maxLen=max(maxLen,len(i))
        
    for i in range(n):
        if len(T[i])<maxLen:
            while len(T[i])<maxLen:
                T[i]=chr(96)+T[i]
    
    return T
       
def countingSort(A,index):
    
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

def radixSort(T,index):
    pass

def strong_string(T):
    pass

T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

reverseStrings(T)
extend(T)
countingSort(T,4)
print(T)


# print(strong_string(T))
# # zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( strong_string, all_tests=False )
