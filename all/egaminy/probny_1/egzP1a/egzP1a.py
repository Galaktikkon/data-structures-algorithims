from egzP1atesty import runtests


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

D = [0, 4, 13, 19, 25]


def titanic(W, M, D):
    # tutaj proszę wpisać własną implementację
    morsed = to_morse(W, M)
    n = len(morsed)
    T = D
    T.remove(4)
    T.remove(19)
    m = len(T)
    F = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(i-4, i):
            pass
    return 0


# runtests(titanic, recursion=False)
