#!/usr/bin/python3
"""The imported modules"""


def rotate_2d_matrix(matrix):
    """The rotate function"""
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)