#!/usr/bin/python3


class Square:

    def __init__(self, size: int = 0, position=(0, 0)):

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

        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value: int):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):

        print("\n"*self.__position[1], end="")
        for i in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))

        if self.__size == 0:
            print()

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value: tuple[int, int]):

        if type(value) is not tuple:
            raise TypeError("value must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("value must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
