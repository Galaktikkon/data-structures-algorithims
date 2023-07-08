from egzP6btesty import runtests

M = ['UL', 'RD', 'LU', 'LU', 'RD', 'DL', 'UR', 'DR']


def create_moveset():
    moveset = {}
    moveset['LU'] = (-1, -2)
    moveset['UL'] = (-2, -1)
    moveset['UR'] = (-2, 1)
    moveset['RU'] = (-1, 2)
    moveset['RD'] = (1, 2)
    moveset['DR'] = (2, 1)
    moveset['DL'] = (2, -1)
    moveset['LD'] = (1, -2)
    return moveset


def jump(M):
    # tutaj proszę wpisać własną implementację
    res = 0
    move_set = create_moveset()
    jumps = [(0, 0)]
    ind = 0
    for j in M:
        v, w = move_set[j]
        jumps.append((jumps[ind][0]+v, jumps[ind][1]+w))
        ind += 1
    lights = {}
    for el in jumps:
        lights[el] = 0
    for el in jumps:
        lights[el] += 1
    for el in lights:
        if lights[el] % 2 == 1:
            res += 1

    return res


# print(jump(M))

runtests(jump, all_tests=True)
