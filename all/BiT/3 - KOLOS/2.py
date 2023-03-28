# tablica k-chaotyczna
# pomysł - zmienić tablicę na krotki z wartoscią i indeksem pierwotny, 
# posortować i porównać indeks właściwy i pierwotny - wziąć maksimum ze wszystkich

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

def convert(A):
    
    n=len(A)
    for i in range(n):
        A[i]=(A[i],i)
   
def kChaotic(A):
    n=len(A)
    convert(A)
    mergeSort(A,0,n-1,0)
    
    k=0
    
    for i in range(n):
        k=max(k,abs(i-A[i][1]))
        
    return k
A=[7,2,3,4,5,6,1]

print(kChaotic(A))
    