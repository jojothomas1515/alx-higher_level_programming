#!/usr/bin/python3
"""Print square module"""

def print_square(size):
    """This function print a square using '#'

    Args:
        size (int): size of the square to print

    """

    if not isinstance(size, int):
        raise (TypeError("size must be an integer"))
    if size < 0:
        raise (ValueError("size must be >= 0"))

    for i in range(size):
        print("{}\n".format("#" * size), end="")


if __name__ == '__main__':
    print_square(5)
