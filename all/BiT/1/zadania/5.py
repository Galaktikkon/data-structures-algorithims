# Dana jest tablica zawierajaca n(n>=11) liczb naturalnych z zakresu [0,k] 
# zamieniono 10 z nich na nowe elementy, ktore sa losowymi liczbami (np. dużo większe/mniejsze)

# Napisać algorytm, który posortuje tablicę w czasie O(n)

# pomysł: podzielić tablice na dwie podtablice, gdzie jedna będzie miała liczby z zakresu, a druga te dodane. 
# Pierwszą można przelecieć counting sortem, drugą czymkolwiek, bo ma stałą długość = 10

A=[0,2000,4,-123,4,2,8000,6,76764,2,312312,7,10,9,8,5,6564,13123,7675,23423,-1000]

def countingSort(A):
    n=len(A)
    k=max(A)
    count=[0 for _ in range(k+1)]
    
    for i in range(n):
        count[A[i]]+=1
    for i in range(1,k+1):
        count[i]+=count[i-1]
                
    output=[0]*n
    
    for i in range(n-1,-1,-1):
        output[count[A[i]]-1]=A[i]
        count[A[i]]-=1
    
    return output

def selectionSort(A):
    n=len(A)
    for i in range(n):
        currMin=i
        for j in range(i+1,n):
            if A[currMin]>A[j]:
                currMin=j
        A[currMin],A[i]=A[i],A[currMin]
    return A

def insertionSort(A):
    n=len(A)
    for i in range(n):
        j=i
        while j>0 and A[j]<A[j-1]:
            A[j],A[j-1]=A[j-1],A[j]
            j-=1
    return A
            
def sort1(A,k):
    n=len(A)
    tabBig=[]
    tabSmall=[]
    for i in range(n):
        if k>=A[i]>=0:
           tabSmall.append(A[i])
        else:
            tabBig.append(A[i])
            
    tabSmall=countingSort(tabSmall)
    tabBig=insertionSort(tabBig)
    print(tabSmall)
    print(tabBig)
    
    i=0
    while tabBig[i]<0:
        A[i]=tabBig[i]
        i+=1
    j=i
    for k in range(i+1,n-10):
        A[i]=tabSmall[k]
        i+=1
    
    while j<10:
        A[i]=tabBig[j]
        i+=1
        j+=1
        
    return A
    
    
print(sort1(A,10))