# Marek Małek 414880

# Algorytm przyjmuje dlugosc slowa i zapisuje w zmiennej n. Jeśli słowo jest puste to zwraca 0. Ustawia zmienne pomocniczne; curr_len 
# jako aktualną długość rozważanego podsłowa oraz max_len jako maksymalną długość. W pętli for przechodzi raz po całym słowie 
# i wyznacza środek rozważanego podsłowa (i), następnie w pętli while zmienne q i p służą do przemieszczania się w odpowiednio 
# lewo i prawo po podsłowie dopóki spełnia wymagania palindromu, po pętli while sprawdza i ewentualnie podmiena wartość max_len, gdy 
# aktualnie rozważane podsłowo,które spełnia warunek palindromu, jest dłuższe. Na koniec zwraca max_len*2 + 1 jeśli znaleziony 
# został przynajmniej jeden palindrom (2*max_len, bo liczymy w curr_len dwie strony na raz, czyli jedną stronę palindromu, a +1, bo
# dodajemy środek, co wszystko opiera się na założeniach, że palindrom jest nieparzysty), w innym przypadku nie ma żadnego palindromu,
# więc najdłuższy palindrom jest długości 1.


# Szacowana złożoność czasowa - O(n^2)
# Szacowania złożoność pamięciowa - O(1)



from zad1testy import runtests

def ceasar(s):
    
    n=len(s)
    
    if n==0:
        return 0
    
    curr_len,max_len=0,0
    
    for i in range(n):
        q=i-1
        p=i+1
        curr_len=0
        
        while q>=0 and p<n and s[q]==s[p]:
            curr_len+=1
            q-=1
            p+=1
            
        max_len=max(max_len,curr_len)
        
    return max_len*2 + 1 if max_len>0 else 1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )