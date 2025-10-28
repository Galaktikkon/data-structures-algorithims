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
from collections import Counter


def get_sieve(number: int) -> list[bool]:
    """
    Computes the Sieve of Eratosthenes up to the given number.
    Returns a list where the index represents the number and the value at that index
    indicates whether it is prime (True) or not (False).

    Args:
        number (int): The upper limit to compute the sieve.
    Returns:
        list[bool]: A list indicating the primality of numbers from 0 to number
    Raises:
        AssertionError: If number is not a non-negative integer or is negative.
    """

    assert isinstance(number, int), "number must be an integer."
    assert number >= 0, "number must be non-negative."

    is_prime: list[bool] = [i >= 2 for i in range(number + 1)]

    for i in range(2, isqrt(number) + 1):
        if is_prime[i]:
            for j in range(i * i, number + 1, i):
                is_prime[j] = False

    return is_prime


def swm(A: list[int], B: list[int]) -> list[int]:
    """
    Returns a sequence C containing all elements from sequence A except those
    that are present in sequence B p times, where p is a prime number.

    Args:
        A (list[int]): The first sequence of integers.
        B (list[int]): The second sequence of integers.
    Returns:
        list[int]: The resulting sequence C.
    """
    counter: Counter[int] = Counter(B)

    if not counter:
        return A[:]

    is_prime: list[bool] = get_sieve(max(counter.values()))

    return [
        number for number in A if number not in counter or not is_prime[counter[number]]
    ]


def test_example_case():
    A = [2, 3, 9, 2, 5, 1, 3, 7, 10]
    B = [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10]
    # From the prompt example
    expected = [2, 9, 2, 5, 7, 10]
    result = swm(A, B)
    assert result == expected


def test_empty_B_returns_copy_of_A_and_not_same_object():
    A = [1, 2, 3]
    B = []
    result = swm(A, B)
    assert result == A
    assert result is not A  # should be a new list (copy)


def test_various_prime_and_nonprime_counts():
    # count of 2 in B is 1 (not prime) => keep 2
    A, B, expected = [1, 2, 3], [2], [1, 2, 3]
    assert swm(A, B) == expected

    # count of 3 in B is 2 (prime) => remove all 3s from A
    A, B, expected = [3, 4, 3, 5], [3, 3], [4, 5]
    assert swm(A, B) == expected

    # count of 7 in B is 3 (prime) => remove all 7s; others kept
    A, B, expected = [7, 1, 7, 2], [7, 7, 7], [1, 2]
    assert swm(A, B) == expected


def test_negative_and_zero_values_handled():
    A = [0, -1, -1, 2, 3]
    B = [-1, -1, 3, 3, 3]  # counts: -1 -> 2 (prime), 3 -> 3 (prime)
    # -1 and 3 should be removed completely from A
    assert swm(A, B) == [0, 2]


def test_large_count_prime_vs_nonprime():
    A = [5, 5, 5, 5, 6]
    # make count of 5 equal to 11 (prime) and count of 6 equal to 12 (non-prime)
    B = [5] * 11 + [6] * 12
    # all 5s removed, 6 kept
    assert swm(A, B) == [6]


if __name__ == "__main__":
    test_example_case()
    test_empty_B_returns_copy_of_A_and_not_same_object()
    test_various_prime_and_nonprime_counts()
    test_negative_and_zero_values_handled()
    test_large_count_prime_vs_nonprime()
