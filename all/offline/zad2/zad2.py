# Marek Małek, 414880

# Aby zebrać jak największą ilość śniegu w jak najkrótszym czasie (tj. zanim się go stopi za dużo)
# najlepiej będzie zbierać go z największych pól wąwozu (tablicy S), zanim upłynie tyle dni, że stopnieje.
# W tym celu zosatły zaimplementowane części algorytmu sortowania przez kopcowanie, funkcje left(), right(), 
# parent(), heapify() oraz buildHeap() służą do zainicjowania i dalszego prowadzania kopca. Na początku budujemy go z tablicy S,
# w efekcie mamy na S[0] największą wartość. Zmienne: n - długość wąwozu (tablicy S), snowSum - ilość zabezpieczonego śniegu,
# melt - ile śniegu stopniało danego dnia oraz 'i' do stymulowania kopcowania. Pętla while działa tak długo, aż rozważany 
# fragment śniegu jest dodatni (czyli jeszcze nie stopniał), w niej dodajemy pole z największym śniegiem (z poprawką na melt)
# dalej, zamieniamy ostatni element z pierwszym, tak jak w algorytmie sortowania oraz go wyrzucamy z tablicy pop'em, 
# aby nie brać tego pola pod uwagę, bo już zebraliśmy z niego śnieg, na koniec naprawiamy strukturę kopca i zwiększamy 
# zmienne melt i 'i'.

# Algorytm działa na zasdzie heapSort'a oraz korzysta z pętli while, która pesymistycznie może mieć złożoność = n, więc:

# Złożoność algorytmu szacuję na O(nlogn+n) = O(nlogn)

from zad2testy import runtests

def right(i): return 2*i+2
def left(i): return 2*i+1
def parent(i): return (i-1)//2

def heapify(A,i,n):
    l=left(i)
    r=right(i)
    max_ind=i
    
    if l<n and A[l]>A[max_ind]: max_ind=l
    if r<n and A[r]>A[max_ind]: max_ind=r
    
    if max_ind!=i:
        A[i],A[max_ind]=A[max_ind],A[i]
        heapify(A,max_ind,n)
        
def buildHeap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)
        
def snow( S ):
    # tu prosze wpisac wlasna implementacje
    
    n=len(S)
    snowSum=0
    melt=0
    i=n-1
    
    buildHeap(S)
    
    while S[0]-melt>0:
        
       snowSum+=S[0]-melt
       
       S[0],S[i]=S[i],S[0]
       
       S.pop(len(S)-1)
       
       heapify(S,0,i)
       
       melt+=1
       i-=1
        
    return snowSum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True)