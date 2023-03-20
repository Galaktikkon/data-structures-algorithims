# SELECTION SORT

def selectionSort(A):
    n=len(A)
    
    for i in range(n):
        
        currMin=i # gdzie jestesmy w tablicy
        
        for j in range(i+1,n): # idziemy po nieposortowanej czesci i szukamy aktualnie najmniejszego elementu
            
            if A[currMin]>A[j]: # podmianka indeksow, jesli znajdziemy cos mniejszego
                currMin=j
                
        A[currMin],A[i]=A[i],A[currMin] 
        # podmieniamy kolejne miejsce w posortowanej czesci na
        # aktualnie najmniejszy element z nieposortowanej czesci
        
    return A
        
    
A=[4, 1, 3, 9, 7]

print(selectionSort(A))