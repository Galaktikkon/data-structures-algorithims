# Kopiec jako kolejka priorytetowa:
# opracje: 
# (stwórz)
# insert - wstaw element
# extract max - wyjmyj element największy

# QUICK SORT
def partition(A,p,r): # wersja locostam (lomuto?XD) ~ LOMUTO
    
    x=A[r] # wybór pivota na ostatni element, tutaj jest ryzyko,
           # że jeżeli tablica jest już posortowana, to wybierzemy największy i będzie złożoność dostaniemy n^2
           
    i=p-1 # wybór na ostatni indeks przed większymi od pivotu
    
    for j in range(p,r): # bo na koncu jest pivot 
        if A[j]<=x:
            i+=1 # przechodzimy na kolejne miejsce, ktore nalezy zamienic
            A[j],A[i]=A[i],A[j] # swap
    A[r],A[i+1]=A[i+1],A[r] # zamiana pivotu z elementem większym od niego 
    
    return i+1 # indeks pivot

# wersja Hoare'a jest sus do implementacji, bo są dwa indeksy i może się coś tam pojebać
        
def quickSort(A,p,r): # p - poczatek, r - koniec przedzialu
    if p<r:
        q=partition(A,p,r) # podział na połowy, gdzie pod q jest pivot
        quickSort(A,p,q-1) # pivotu nie trzeba uwzględniać, bo jest na swoim miejscu
        quickSort(A,q+1,r)
    
A=[1,3,4,2,56,7,6,2,4,5,1,3,2,6,4,3,2,6,64,3,2,4,7]

quickSort(A,0,len(A)-1)

print(A)

# ryzyko: 
# przy algorytm może się ukwadratawiać, przy pechowych wyborach pivotu, a to może doprowadzić do zapchania stosu przy rekurencji

# QUICK SORT bez rekurenkcji ogonowej - zmniejszenie ryzyka zapchania stosu

def quickSort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        quickSort(A,p,q-1)  # na początku zajmujemy się lewą częścią
        p=q+1               # chcemy wywołać quickSort(A,q+1,r)
        
        
# STATYSTKI POZYCYJNE
