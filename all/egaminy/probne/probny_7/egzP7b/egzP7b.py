from egzP7btesty import runtests

S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V = [5, 3, 6, 6]


def ogrod(S, V):
    # Tutaj proszę wpisać własną implementację
    n = len(S)
    m = len(V)
    result, sub_result = 0, 0
    for i in range(n):
        sub_result = 0
        status = [0 for _ in range(m)]
        for j in range(i, n):
            if status[S[j]-1] == 0:
                sub_result += V[S[j]-1]
                status[S[j]-1] = 1
            elif status[S[j]-1] == 1:
                result = max(result, sub_result)
                sub_result -= V[S[j]-1]
                status[S[j]-1] = 2
            elif status[S[j]-1] == 2:
                pass

        result = max(result, sub_result)

    return result


# print(ogrod(S, V))


runtests(ogrod, all_tests=True)
