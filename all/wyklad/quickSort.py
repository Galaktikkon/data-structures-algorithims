def partition(A,p,r):
    
    x=A[r] 
           
    i=p-1 
    
    for j in range(p,r): 
        if A[j]<=x:
            i+=1 
            A[j],A[i]=A[i],A[j] 
    A[r],A[i+1]=A[i+1],A[r]
    
    return i+1 

def quickSort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1) 
        p=q+1   