#!/usr/bin/python3


"""This is a module level documentation

My checker has been failing even tho the ouput is the same,
i hope this is the cause.
"""


class Square:
    """Creates a square object.

    This class makes a square object with the
    necessary attr for a square to allow for computation.
    """

    def __init__(self, size: int):
        """Square object constructor

        Args:
            size (int): The size of the square
        """
        self.__size = size
