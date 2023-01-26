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

    def __init__(self, size: int = 0, position=(0, 0)):
        """Square object constructor

        Args:
            size : The size of the square
            position : print position
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """The print position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the print position tuple

        Args:
            value : tuple of integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int) or
                  isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((value[0] < 0) or
              (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print the square to stdout as '#'

        If the size is 0 print a newline
        """
        if self.__size == 0:
            print()
            return
        print("\n"*self.position[1], end="")
        for i in range(self.__size):
            print("{}{}".format(" "*self.position[0], "#"*self.size))


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
