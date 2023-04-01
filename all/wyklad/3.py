# counting sort

A=[2,0,3,1,1,2,3,2,5,3,2,4,3,3,22,1,4,2,3,77,4,23,12,45,23,6,5,12,66,8,9,0,3,12,43,55,67,3,83,3,82,13,98,56,24,23,12,34,356,97,67,8,67]

def countingSort(A,k):
    n=len(A)
    
    C=[0]*k
    B=[0]*n
    
    for i in range(n):
        C[A[i]]+=1
    
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
        
    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
        
    return B

# print(countingSort(A,4))


# RADIX SORT

# A=['kra','art','ort','kot','kit','ati','kil']

# pomysl - counting sort po ostatnich literach, bo znamy przedział danych

# sortowanie n słów, kazde o długości t, zajęło O(nt) czasu

# BUCKET SORT

# A - tablica liczb wymiernych, 0<=A[i]<1, elementy A byly wygenerowane zgodnie z rozkladem jednostajnym, n - rozmiar tablicy
# Tworzymy n wiader (list), wiadro 0 ma zakres [0,1/n), wiadro 1 ma zakres [1/n, 2/n) ... wiadro n-1 [(n-1)/n, n/n)
# Przeglądamy tablicę A i aktualną liczbę A[i] umieszczamy w wiadrze floor(n*A[i]), każde wiadro sortujemy (np. sortowania prostego)
# Przepisujemy dane do A z wiader w kolejności

# oczekiwana złożoność - O(n)

# MAGICZNE PIĄTKI

# Magiczne Piątki - wybór k-tego elementu w czasue O(n) bez ryzyka "ukwadratowienia"
# A - tablica n liczb, chcemy znaleźć liczbę, która po posortowaniu byłaby na k-tej pozycji.
# 1. Podziel wejściową tablicę (A), na ceil(n/5) grup, po pięć elementów.
# 2. Dla każdej z tych grup, znajdujemy medianę.
# 3. Rekurencyjnie znajduję x - medianę wśród median naszych piątek.
# 4. Wykonaj partition() używając x jako pivot.
# 5. Jeśli x jest na pozycji k-tej, to zwróć x
# 6. Jeśli x jest na pozycji dalszej niż k, to szukaj rekurencyjnie na lewej części tablicy
# 7. W pp. w prawej części tablicy.

import math

def selectionSort(A):
    n=len(A)
    
    for i in range(n):
        
        currMin=i 
        
        for j in range(i+1,n): 
            
            if A[currMin]>A[j]: 
                currMin=j
                
        A[currMin],A[i]=A[i],A[currMin] 

    return A

def divIntoGroups(A):
    n=len(A)
    output=[[] for _ in range(math.ceil(n/5))]
    
    for i in range(n):
        output[i//5].append(A[i])
    
    for i in range(len(output)):
        output[i]=selectionSort(output[i])
    
    return output

def partition(A,p,r,pivotIndex):
    
    x=A[pivotIndex] 
           
    i=p-1 
    
    for j in range(p,r): 
        if A[j]<=x:
            i+=1 
            A[j],A[i]=A[i],A[j] 
    A[r],A[i+1]=A[i+1],A[r]
    
    return i+1 

def select(A,k,p,r):
    
    q=partition(A,p,r,r-1)
    
    if q==k:
        return q
    
    elif q>k:
        return select(A,k,p,q-1)
        
    elif q<k:
        return select(A,k,q+1,r)

def findMedian(A):
    medians=[]
    for i in range(len(A)):
        medians.append(A[i][len(A[i])//2])
    n=len(medians)
    return select(medians,n//2,0,n-1)

def MagicSelect(A,p,r,k):
    A=A[p:r]
    q=partition(A,p,r,findMedian(divIntoGroups(A)))
    
    if q==k:
        return A[q]
    elif q>k:
        return MagicSelect(A,p,q-1,k)
    elif q<k:
        return MagicSelect(A,q+1,r,k)
    
def MagicFives(A,k):
    return MagicSelect(A,0,len(A)-1,k)

B=[i for i in range(101)]

# print(MagicFives(B,99))

for i in range(len(B)):
    print(MagicFives(B,i),i)