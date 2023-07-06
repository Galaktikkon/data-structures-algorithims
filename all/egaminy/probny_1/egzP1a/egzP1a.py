from egzP1atesty import runtests
from math import inf


def to_morse(W, M):
    morsed = ''
    for letter in W:
        morsed += M[ord(letter)-ord('Z')-1][1]
    return morsed


M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'),
     ('G', '--.'), ('H', '....'), ('I', '..'), ('J',
                                                '.---'), ('K', '-.-'), ('L', '.-..'),
     ('M', '--'), ('N', '-.'), ('O', '---'), ('P',
                                              '.--.'), ('Q', '--.-'), ('R', '.-.'),
     ('S', '...'), ('T', '-'), ('U', '..-'), ('V',
                                              '...-'), ('W', '.--'), ('X', '-..-'),
     ('Y', '-.--'), ('Z', '--..')]

print(to_morse('SOS', M))
W = 'SOS'
D = [0, 4, 13, 19, 25]


def titanic(W, M, D):
    # tutaj proszę wpisać własną implementację
    morsed = to_morse(W, M)
    n = len(morsed)
    m = len(D)
    print(D)
    # print(morsed)
    F = [0 for _ in range(n)]
    F[1] = 1
    for i in range(1, n):
        F[i] = n
        for j in range(m):
            sign = M[D[j]][1]
            if i-len(sign) >= 0 and morsed[i-len(sign)+1:i+1] == sign:
                if F[i-len(sign)]+1 < F[i]:
                    F[i] = F[i-len(sign)]+1
    return F[n-1]


runtests(titanic, recursion=False)
