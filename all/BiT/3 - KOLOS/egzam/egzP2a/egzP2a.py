from egzP2atesty import runtests 

def partition(A,p,r):
    
    x=A[r]
    
    i=p-1
    
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def quickSelect(A,p,r,k):
    
    q=partition(A,p,r)
    
    if q==k:
        return A[q]
    elif q>k:
        return quickSelect(A,p,q-1,k)
    elif q<k:
        return quickSelect(A,q+1,r,k)


def zdjecie(T, m, k):
    #tutaj proszę wpisać własną implementację
    n=len(T)
    p=0
    r=n-1
    i=0
    while i<m:
        quickSelect(T,p,r,k+i+i*m)
        p+=k+i
        i+=1
    
    return None


runtests ( zdjecie, all_tests=False )