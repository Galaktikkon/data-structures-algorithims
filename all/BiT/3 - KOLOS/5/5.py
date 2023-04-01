from Exercise_2_tests import runtests

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def right(i): return 2*i+2
def left(i): return 2*i+1
def parent(i): return (i-1)//2

def heapify(A,i,n):
    l=left(i)
    r=right(i)
    min_ind=i
    
    if l<n and A[l]<A[min_ind]: min_ind=l
    if r<n and A[r]<A[min_ind]: min_ind=r
    
    if min_ind!=i:
        A[i],A[min_ind]=A[min_ind],A[i]
        heapify(A,min_ind,n)
        
def buildHeap(A,k):
    for i in range(parent(k-1),-1,-1):
        heapify(A,i,k)

def sortH(p,k):
    k+=1
    A=[0]*k

    G=Node(None)
    o=G    
    for i in range(k):
        A[i]=p.val
        p=p.next
        
    buildHeap(A,k)
    
    while p is not None:
        N=Node(A[0])
        G.next=N
        G=G.next
        A[0]=p.val
        p=p.next
        heapify(A,0,k)
        
    while A[0] != float('inf'):
        N=Node(A[0])
        G.next=N
        G=G.next
        A[0]=float('inf')
        heapify(A,0,k)
    
    return o.next
    
g=Node(5)    
f=Node(6,g) 
e=Node(4,f) 
d=Node(2,e) 
c=Node(3,d) 
b=Node(0,c) 
a=Node(1,b)
   
def printList(p):
    p=p.next if p.val is None else p
    while p is not None:
        print(p.val,end=' ')
        p=p.next

# printList(sortH(a,1))
# runtests(sortH)