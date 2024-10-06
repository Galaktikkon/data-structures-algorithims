# Task:
# Write a function that receives two sequences: A and B of integers and returns one sequence C.
# Sequence C should contain all elements from sequence A (maintaining the order) except those,
# that are present in sequence B p times, where p is a prime number.

# Example:
# A = [2, 3, 9, 2, 5, 1, 3, 7, 10]

# B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]

# C = [2, 9, 2, 5, 7, 10]


# Notes:

# 1. The time complexity is important – try to write an algorithm with good time complexity and specify it in your answer.

# 2. You can choose any reasonable type present in your chosen language to represent the sequence.

# 3. Make sure the function signature is correct.

# 4. Write your own code to test primality.

# 5. Make sure your code is not outputting anything on standard output. If you want to leave us a hint how to run your code - place it in a comment.

from math import isqrt


def is_prime(number):

    if number <= 3:
        return number >= 2

    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(5, isqrt(number)+1, 6):
        if number % i == 0 or number % (i+2) == 0:
            return False

    return True


def swm(A, B):

    C = []

    counter = {}

    for number in B:
        if number not in counter:
            counter[number] = 1
        else:
            counter[number] += 1

    for number in A:
        if number not in counter:
            C.append(number)
        elif not is_prime(counter[number]):
            C.append(number)

    return C


A = [2, 3, 9, 2, 5, 1, 3, 7, 10]

B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]

C = [2, 9, 2, 5, 7, 10]

assert swm(A, B) == C
