#!/usr/bin/python3

"""This is a module level documentation

My checker has been failing even tho the ouput is the same,
i hope this is the cause.
"""


from turtle import pos


class Square:
    """Creates a square object.

    This class makes a square object with the
    necessary attr for a square to allow for computation.
    """

    def __init__(self, size: int = 0, position=(0, 0)):
        """Square object constructor

        Args:
            size : The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
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

    def my_print(self):
        """print the square to stdout as '#'

        If the size is 0 print a newline
        """
        for i in range(self.__size):
            print("#"*self.__size)

        if self.__size == 0:
            print()


if __name__ == '__main__':
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
