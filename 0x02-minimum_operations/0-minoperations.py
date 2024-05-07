#!/usr/bin/python3
""" The imported modules """


def minOperations(n: int) -> int:
    """ The function definition
    Args:
        n: the input
    """
    a = 'H'
    b = 'H'
    op = 0
    while (len(b) < n):
        if n % len(b) == 0:
            op += 2
            a = b
            b += b
        else:
            op += 1
            b += a
    if len(b) != n:
        return 0
    return op
