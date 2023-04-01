from zad2testy import runtests

# def partition(A,p,r):
    
#     x=A[r]
    
#     i=p-1
    
#     for j in range(p,r):
#         if A[j]<=x:
#             i+=1
#             A[i],A[j]=A[j],A[i]
#     A[i+1],A[r]=A[r],A[i+1]
    
#     return i+1

# def quickSelect(A,p,r,k):
    
#     q=partition(A,p,r)
    
#     if q==k:
#         return A[q]
#     elif q>k:
#         return quickSelect(A,p,q-1,k)
#     elif q<k:
#         return quickSelect(A,q+1,r,k)

# def quickSort(A,p,r):
#     while p<r:
#         q=partition(A,p,r)
#         quickSort(A,p,q-1) 
#         p=q+1

def right(i): return 2*i+2
def left(i): return 2*i+1
def parent(i): return (i-1)//2

def heapify(A,i,n,key,type):
    if type==0:
        l=left(i)
        r=right(i)
        max_ind=i

        if l<n and A[l][key]>A[max_ind][key]: max_ind=l
        if r<n and A[r][key]>A[max_ind][key]: max_ind=r

        if max_ind!=i:
            A[i],A[max_ind]=A[max_ind],A[i]
            heapify(A,max_ind,n,key,type)
    elif type==1:
        l=left(i)
        r=right(i)
        min_ind=i

        if l<n and A[l][key]<A[min_ind][key]: min_ind=l
        if r<n and A[r][key]<A[min_ind][key]: min_ind=r

        if min_ind!=i:
            A[i],A[min_ind]=A[min_ind],A[i]
            heapify(A,min_ind,n,key,type)
        
def buildHeap(A,key,type):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n,key,type)
    #budowanie od dołu, tworzy sie kopiec z wezlem, kotry jest rodzicem ostatniego indeksu, i dalej petla od konca 
    
def heapSort(A,key,type):
    n=len(A)
    buildHeap(A,key,type)
    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i,key,type)
        

def depth(L):
    # tu prosze wpisac wlasna implementacje
    n=len(L)
    heapSort(L,1,0)
    heapSort(L,0,0)
    
    



L=[[1, 6],[5, 6],[2, 5],[8, 9],[1, 6]]

depth(L)

print(L)

# runtests( depth ) 
