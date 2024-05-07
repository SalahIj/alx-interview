#!/usr/bin/python3
""" Imported modules """


def minOperations(n):
    """The function definition
    Args:
        n: the input
    """
    if not isinstance(n, int):
        return 0
    a = 0
    b = 0
    c = 1
    while c < n:
        if b == 0:
            b = c
            c += b
            a += 2
        elif n - c > 0 and (n - c) % c == 0:
            b = c
            c += b
            a += 2
        elif b > 0:
            c += b
            a += 1
    return a
