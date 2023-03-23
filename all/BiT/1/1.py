# SORTOWANIA LINIOWE

# stabilnosc sortowania - zachowana kolejnosc elementow sobie równych np:
# [(1,2),(0,1),(2,2)] -(sortowanie po 'y')-> [(0,1),(1,2),(2,2)]


# COUNTING SORT

# wymagania: zakres wartoci ograniczony do liczb naturalnych [0,k]

def countingSort(A,B,k):
    n=len(A)
    C=[0 for _ in range(k+1)]
    for i in range(n):              #zliczanie ilosci elementow o danej wartosci
        C[A[i]]+=1      
    for i in range(1,k+1):          #gwarancja stabilności teraz na i-tej pozycji jest zapisane ile jest elementow =>i
        C[i]+=C[i-1]        
    for i in range(n-1,-1,-1):       #spisywanie od końca z pomoca tablicy C, w przypadku kilku takich samych wartosci sa wpisywane 
        B[C[A[i]]-1]=A[i]           #tez od konca z pierwsza wpisana na ostatnie mozliwe miejsce
        C[A[i]]-=1
    return B

A=[2,2,5,4,1,7,5,3,2,1,5,3,2,3,3,4,0,0,0]
B=[0]*len(A)

# print(countingSort(A,B,7))


# RADIX SORT

# wymagania: dane podobnej długości, muszą się dać posortować leksykograficznie

def radixSort(A,d):
    for i in range(1,d):
        pass # sortowanie po i-tej cyfrze/znaku 
    
    
    
# BUCKET SORT

# wymagania: liczby z zakresu [0,1] ([0,k] z normalizacją), musimy znać liczbę kubełków, rozkład jednostajny

def bucketSort(A,n):
    norm=max(A)
    buckets=[[] for _ in range(n)] # tworzenie n kubełków
    
    for num in A:
        normNum=num/norm # znormalizowana wartośc
        bucketInd=int(n*normNum -1 if normNum*n>0 else 0) # wybór kubełka
        buckets[bucketInd].append(num) 
        
    for i in range(n): # sortowanie wartości w kubełkach
        buckets[i]=sorted(buckets[i])
        
    output=[]
    
    for i in range(n):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
            
    return output
        
# print(bucketSort(A,len(A)))

