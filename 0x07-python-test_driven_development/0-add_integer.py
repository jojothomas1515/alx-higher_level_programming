#!/usr/bin/python3
"""Add integer module """

def add_integer(a, b=98):
    """add_integer function

    Args:
        a (int): first argument
        b (int): second argument

    Return: The sum of a and b

    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise (TypeError("a must be an integer"))
    if not (isinstance(b, int) or isinstance(b, float)):
        raise (TypeError("b must be an integer"))

    return (int(a) + int(b))


if __name__ == '__main__':
    print(add_integer(22, nan))
