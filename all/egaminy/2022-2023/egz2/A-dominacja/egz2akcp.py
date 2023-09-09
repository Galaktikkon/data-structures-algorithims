from egz2atesty import runtests


def dominance(P):
    max_dom = 0
    curr_dom = 0
    n = len(P)
    for i in range(n):
        curr_dom = 0
        for j in range(n):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                curr_dom += 1
        max_dom = max(max_dom, curr_dom)

    return max_dom


runtests(dominance, all_tests=True)
