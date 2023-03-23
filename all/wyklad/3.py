# counting sort

A=[2,0,3,1,1,2,3,2]

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

print(countingSort(A,4))


# RADIX SORT

A=['kra','art','ort','kot','kit','ati','kil']

# pomysl - counting sort po ostatnich literach, bo znamy przedział danych

# sortowanie n słów, kazde o długości t, zajęło O(nt) czasu

# BUCKET SORT

# A - tablica liczb wymiernych, 0<=A[i]<1, elementy A byly wygenerowane zgodnie z rozkladem jednostajnym, n - rozmiar tablicy
# Tworzymy n wiader (list), wiadro 0 ma zakres [0,1/n), wiadro 1 ma zakres [1/n, 2/n) ... wiadro n-1 [(n-1)/n, n/n)
# Przeglądamy tablicę A i aktualną liczbę A[i] umieszczamy w wiadrze floor(n*A[i]), każde wiadro sortujemy (np. sortowania prostego)
# Przepisujemy dane do A z wiader w kolejności

# oczekiwana złożoność - O(n)

# Magiczne Piątki - wybór k-tego elementu w czasue O(n) bez ryzyka "ukwadratowienia"
# A - tab  