#  1. Dana jest tablica n liczb ze zbioru [0,n^2-1], posortować jak najszybciej
#  2. Dana jest tablica n liczb zawierająca O(logn) różnych wartości, posortować jak najszybciej
#  3. Dana jest tablica n liczb, szukamy takich dwóch, które po posortowaniu byłyby koło siebie oraz ich różnica jest maksymalna.
#  4. Dane sa dwa napisy, zaimplementowac funkcję sprawdzającą czy są anagramami.
#  5. Mamy tablicę T rozmiaru n, T[i] zawiera się w {0,...,k-1}, chcemy najmniejszy podprzedział, który zawiera wszystkie kolory.
#  6. wartosć od 0-10^9-1, losowane są serie danych z tego przedziału, trzeba zliczyć ile w serii jest powtarzających się wartości.
#  7. znalezienie najmniejszego wielokąta wypukłego, który obejmuje wszystkie punkty - problem otoczki wypukłej
# ad 1.
# radix sort po 1) %n i 2) //n
# ad 2.
# tablica tablic, zawierajaca informacje ile razy wystapila liczba w glownej tablicy, (wyszukiwanie binarne)jak jest to dodajemy,
# jak nie to wstawiamy, n razy wstawiwamy liczbe wyszukujac binarne log od logn liczb - nlog(logn)
# ad 3. podział na n kubełków, i szukanie min max w zależności od sytuacji.
# ad 5. dwoma wskaźnikami
