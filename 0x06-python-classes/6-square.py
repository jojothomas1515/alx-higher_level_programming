#!/usr/bin/python3

"""This is a module documentation

This is so fucked up
"""


class Square:
    """Square class

    Use for creating Square object instance

    Example:
        square_1 : Square = Square(10,(1,1))
    """

    def __init__(self, size: int = 0, position=(0, 0)):
        """Square Constructor

        Initializing function

        Args:
            size (int): size of the square
            position (tuple): display position
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(position[0], int) or
                isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Square Area

        Computes the area of a Square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Returns Size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value: int):
        """Set the size of the square

        Args:
            value (int): the new size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square followed by a newline."""

        print("\n"*self.__position[1], end="")
        for i in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))

        if self.__size == 0:
            print()

    @property
    def position(self):
        """ Returns Print Position."""
        return (self.__position)

    @position.setter
    def position(self, value: tuple[int, int]):
        """Position Setter

        Args:
            value (tuple): new position tuple

        Description:
            Sets the new position
        """

        if type(value) is not tuple:
            raise TypeError("value must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("value must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
