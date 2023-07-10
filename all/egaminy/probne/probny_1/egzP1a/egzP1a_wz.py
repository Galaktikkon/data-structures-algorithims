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

# print(to_morse('SOS', M))
# W = 'SOS'
# D = [0, 4, 13, 19, 25]


def titanic(W, M, D):
    # tutaj proszę wpisać własną implementację
    morsed = to_morse(W, M)
    dic = {}
    n = len(morsed)
    m = len(D)
    for i in range(m):
        dic[M[D[i]][1]] = len(M[D[i]][1])
    F = [n for _ in range(n+1)]
    F[0] = 1
    F[-1] = 0
    for i in range(1, n):
        for j in range(5):
            if morsed[i-j+1:i+1] in dic:
                F[i] = min(F[i], F[i-j]+1)
    return F[n-1]


# print(titanic(W, M, D))
runtests(titanic, recursion=False)
