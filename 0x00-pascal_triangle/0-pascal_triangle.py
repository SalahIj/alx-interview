def pascal_triangle(n):
    """ Pascal function
    Args:
        n: the input of the pascal function
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle


def print_triangle(triangle):
    """ Printing the triangle
    Args:
        triangle: the printing triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
