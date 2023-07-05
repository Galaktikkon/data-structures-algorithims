def reverseWords(S):
    # code here
    n = len(S)
    reversed = ''
    i, j = n-1, n
    while i >= 0:
        chunk = ''
        while S[i] != '.' and i >= 0:
            chunk = S[i]+chunk
            i -= 1
        if i > 0:
            reversed += chunk+"."
        else:
            reversed += chunk
        i -= 1
    return reversed


# S='i.like.this.program.very.much'
S = 'pqr.mno'
print(reverseWords(S))
