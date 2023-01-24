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

    def __init__(self, size: int = 0):
        """Square object constructor

        Args:
            size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of a square

        Return:
            int: the current square area.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value: int):
        """Sets the value for size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
