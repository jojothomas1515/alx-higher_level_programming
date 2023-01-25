#!/usr/bin/python3

"""
This is a module level documentation

My checker has been failing even tho the ouput is the same,
i hope this is the cause.
"""


class Square:
    """Creates a square object.

    This class makes a square object with the
    necessary attr for a square to allow for computation.
    """

    def __init__(self, size: int = 0, position: tuple[int, int] = (0, 0)):
        """Square object constructor

        Args:
            size (int): The size of the square
            position (tuple[int, int]): The position of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        """Calculate the area of a square

        Return:
            int: the current square area.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Returns the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value: int):
        """Sets the value for size


        Args:
            value (int): new value for size.
        ."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print the square to stdout as '#'

        If the size is 0 print a newline.
        """

        for i in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))

        if self.__size == 0:
            print()

    @property
    def position(self):
        """Returns instance square postion."""
        return (self.__position)

    @position.setter
    def position(self, value: tuple[int, int]):
        """Setting the value for position

        Args:
            value (tuple): new postion value.
        """
        if type(value) is not tuple:
            raise TypeError("value must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("value must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
