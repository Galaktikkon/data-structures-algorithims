from egzP5atesty import runtests

T = [2, 1, 5, 6, 2, 3]


def inwestor(T):
    # tutaj proszę wpisać własną implementację
    n = len(T)
    stack = [-1, 0]
    left = [-1 for _ in range(n)]
    right = [n for _ in range(n)]
    result = 0
    for i in range(1, n):
        while T[stack[len(stack)-1]] > T[i] and stack[len(stack)-1] != -1:
            right[stack[len(stack)-1]] = i
            stack.pop()

        if T[i] == T[i-1]:
            left[i] = left[i-1]

        else:
            left[i] = stack[len(stack)-1]

        stack.append(i)

    for i in range(n):
        result = max(result, (right[i]-left[i]-1)*T[i])

    return result


runtests(inwestor, all_tests=True)
