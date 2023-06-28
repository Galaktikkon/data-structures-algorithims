def longest_common(x, y, s1, s2):
    F = [[0 for _ in range(x+1)]for _ in range(y+1)]
    for i in range(1, y+1):
        for j in range(1, x+1):
            if s1[j-1] == s2[i-1]:
                F[i][j] = F[i-1][j-1]+1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F


s1 = 'AAPAHJWTESPLWEQFMNMYMTQ'
s2 = 'RELEIN'

# s1 = 'GEBEOCFUFTSXDIXTIGSIEEHKCHZ'
# s2 = 'DFLILRJQFNXZ'

# s1 = 'AWITXYSJQZNCIPTTNC'
# s2 = 'JTJHRTVKW'


def print_res(F, s1, s2):
    print("      ", end='')
    for letter in s1:
        print(letter, " ", end='')
    print()
    for i in range(len(F)):
        if i > 0:
            print(s2[i-1], "", end='')
        else:
            print("  ", end='')
        print(F[i])


print_res(longest_common(len(s1), len(s2), s1, s2), s1, s2)
