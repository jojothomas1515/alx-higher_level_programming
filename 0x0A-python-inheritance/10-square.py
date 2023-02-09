#!/usr/bin/python3

"""Base Geometry Module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class """

    def __init__(self, size):
        """
        Square constructor
        :param size: size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super(Square, self).__init__(size, size)


if __name__ == '__main__':
    print(issubclass(Square, Rectangle))
