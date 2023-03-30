def right(i): return 2*i+2
def left(i): return 2*i+1
def parent(i): return (i-1)//2

def heapify(A,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    
    if l<n and A[l]>A[max_ind]: max_ind=l
    if r<n and A[r]>A[max_ind]: max_ind=r
    
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,max_ind,n)
        
def buildHeap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)
    
def heapSort(A):
    n=len(A)
    buildHeap(A)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)

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
        
def quickSelect(A,k,p,r):
    
    q=partition(A,p,r)
    
    if q==k:
        return A[q]
    
    elif q>k:
        return quickSelect(A,k,p,q-1)
        
    elif q<k:
        return quickSelect(A,k,q+1,r)
    
def countingSort(A,B,k):
    n=len(A)
    C=[0 for _ in range(k+1)]
    for i in range(n):
        C[A[i]]+=1
    for i in range(1,k+1):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    return B

def bucketSort(A,n):
    norm=max(A)
    buckets=[[] for _ in range(n)] 
    
    for num in A:
        normNum=num/norm 
        bucketInd=int(n*normNum -1 if normNum*n>0 else 0) 
        buckets[bucketInd].append(num) 
        
    for i in range(n):
        buckets[i]=sorted(buckets[i])
        
    output=[]
    
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
            
    return output

def merge(A,left,mid,right,index):
    
    n1=mid-left+1
    n2=right-mid
    
    L=[0 for _ in range(n1)]    
    R=[0 for _ in range(n2)]
    
    for i in range(n1):
        L[i]=A[i+left]
    
    for i in range(n2):  
        R[i]=A[i+mid+1]
        
    sortIndex=left
    i,j=0,0
    
    while i<n1 and j<n2:
        if L[i][index]<=R[j][index]:
            A[sortIndex]=L[i]
            i+=1
        else:
            A[sortIndex]=R[j]
            j+=1
        sortIndex+=1
    
    while i<n1:
        A[sortIndex]=L[i]
        i+=1
        sortIndex+=1
    while j<n2:
        A[sortIndex]=R[j]
        j+=1
        sortIndex+=1

def mergeSort(A,left,right,index):
    if left<right:
        mid=(left+right)//2    
        mergeSort(A,left,mid,index)
        mergeSort(A,mid+1,right,index)
        merge(A,left,mid,right,index)

import collections
