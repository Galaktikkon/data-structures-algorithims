# Kopiec jako kolejka priorytetowa:
# opracje:
# (stwórz)
# insert - wstaw element
# extract max - wyjmyj element największy

# QUICK SORT
def partition(A, p, r):  # wersja locostam (lomuto?XD) ~ LOMUTO

    x = A[r]  # wybór pivota na ostatni element, tutaj jest ryzyko,
    # że jeżeli tablica jest już posortowana, to wybierzemy największy i będzie złożoność dostaniemy n^2

    i = p-1  # wybór na ostatni indeks przed większymi od pivotu

    for j in range(p, r):  # bo na koncu jest pivot
        if A[j] <= x:
            i += 1  # przechodzimy na kolejne miejsce, ktore nalezy zamienic
            A[j], A[i] = A[i], A[j]  # swap
    A[r], A[i+1] = A[i+1], A[r]  # zamiana pivotu z elementem większym od niego

    return i+1  # indeks pivot

# wersja Hoare'a jest sus do implementacji, bo są dwa indeksy i może się coś tam pojebać


def quickSort(A, p, r):  # p - poczatek, r - koniec przedzialu
    if p < r:
        q = partition(A, p, r)  # podział na połowy, gdzie pod q jest pivot
        # pivotu nie trzeba uwzględniać, bo jest na swoim miejscu
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


# A = [1, 3, 4, 2, 56, 7, 6, 2, 4, 5, 1, 3, 2, 6, 4, 3, 2, 6, 64, 3, 2, 4, 7]

# quickSort(A, 0, len(A)-1)

# print(A)

# ryzyko:
# przy algorytm może się ukwadratawiać, przy pechowych wyborach pivotu, a to może doprowadzić do zapchania stosu przy rekurencji

# QUICK SORT bez rekurenkcji ogonowej - zmniejszenie ryzyka zapchania stosu


def quickSort2(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quickSort2(A, p, q-1)  # na początku zajmujemy się lewą częścią
        p = q+1               # chcemy wywołać quickSort(A,q+1,r)


# STATYSTKI POZYCYJNE

# zastosowanie funkcji partition do obliczania statystkyk pozycyjnych

# k-ta statystyka pozycyjna, element A, który byłby na k-tej pozycji po posortowaniu, w szczególności:
# select(A,0) = min(A)
# select(A,len(A)-1) = max(A)
# select(A,(len(A))/2) = mediana A
# A=[1,3,"8",9,16]
# A=[1,"4","7",20]

# złożoność czasowa - O(n)

def select(A, k, p, r):

    q = partition(A, p, r)

    if q == k:
        return A[q]

    elif q > k:
        return select(A, k, p, q-1)

    elif q < k:
        return select(A, k, q+1, r)


A = [7, 10, 4, 20, 15, 12, 23, 5, 1, 2, 55, 34, 11, 26, 14, 30, 31, 42]

print(select(A, 5, 0, len(A)-1))
print(A)
print(select(A, 9, 5, len(A)-1))
print(A)
