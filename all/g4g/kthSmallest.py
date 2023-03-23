# kurwa
# werjsa z heapem ehh
def kthSmallest(arr, l, r, k):
    n=len(arr)
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    def right(i): return 2*i+2
    def left(i): return 2*i+1
    def parent(i): return (i-1)//2
    
    def heapifyMax(A,i,n):
        r=right(i)
        l=left(i)
        maxInd=i
        
        if l<n and A[maxInd]<A[l]: maxInd=l
        if r<n and A[maxInd]<A[r]: maxInd=r
        
        if maxInd!=i:
            A[i],A[maxInd]=A[maxInd],A[i]
            heapifyMax(A,maxInd,n)
    
    def heapifyMin(A,i,n):
        r=right(i)
        l=left(i)
        minInd=i
        
        if l<n and A[minInd]>A[l]: minInd=l
        if r<n and A[minInd]>A[r]: minInd=r
        
        if minInd!=i:
            A[i],A[minInd]=A[minInd],A[i]
            heapifyMin(A,minInd,n)
    
    if k>n//2:
        for i in range(n-1,-1,-1):
            heapifyMax(arr,i,n)
        for i in range(n-1,n-k-1,-1):
            arr[0],arr[i]=arr[i],arr[0]
            heapifyMax(arr,0,i)
        print(arr)
        return arr[k-1]
    
    else:
        for i in range(n-1,-1,-1):
            heapifyMin(arr,i,n)
        
        for i in range(n-1,n-k-1,-1):
            arr[0],arr[i]=arr[i],arr[0]
            heapifyMin(arr,0,i)
        print(arr)
        return arr[n-k]

A=[7, 10, 4, 20, 15]

print(kthSmallest(A,0,len(A)-1,4))

# wersja z selectem POG
def kthSmallest(arr, l, r, k):
    
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    
    def partition(A,p,r):
        
        x=A[r]
        
        i=p-1
        
        for j in range(p,r):
            if A[j]<=x:
                i+=1
                A[j],A[i]=A[i],A[j]
                
        A[r],A[i+1]=A[i+1],A[r]
        
        return i+1
    
    def select(A,l,r,k):
        
        q=partition(arr,l,r)
    
        if q+1==k:
            return A[q]
        
        elif q+1>k:
            return select(A,l,q-1,k)
        elif q+1<k:
            return select(A,q+1,r,k)
    
    return select(arr,l,r,k)