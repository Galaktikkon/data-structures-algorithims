# Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem danego języka.
# Dostajemy na wejściou stringa bez spacji. Podaj algorytm, który stwierdzi czy da się tak powstawiać spacje do wejściowego stringa,
# że ciąg słów, który otrztmamy tworzą słowa z danego języka. Np. "alamakotainiemapsa" możemy zapisać jako "ala ma kota i nie ma psa".
# Podaj również jak wykorzystać algorytm, aby uzyskać przykładowe poprawne rozdzielenie stringa spacjami, jeśli oczywiście ono istnieje.
# Algorytm ma być szybki, ale najważniejsze, żeby był poprawny.

# Rozwiązanie:
# podejście jak ze sprawdzaniem podsłów(f(i,j) - słowo od i-j), póżniej zaczynamy od końca i jeżeli f(i,j) jest poprawne,
# to skaczemy do słowa mniejszego i sprawdzamy czy da się dojść do słowa pustego.
