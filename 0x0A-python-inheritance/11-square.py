#!/usr/bin/python3

"""Base Geometry Module"""


class BaseGeometry:
    """
    Base Geometry class, from while other
    classes are to be subclassed from
    """

    def area(self):
        """The area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):
        """
        The method validates value

        :param name: a name string
        :param value: value to validates
        """
        if not value.__class__ == int:
            raise TypeError("{} must be an integer".format(str(name)))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(str(name)))


class Rectangle(BaseGeometry):
    """Rectangle class, subclassed from base geometry"""

    def __init__(self, width, height):
        """
        Rectangle Constructor

        :param width: width to be set
        :param height: height to be set
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def integer_validator(self, name: str, value):
        super().integer_validator(name, value)

    def area(self):
        """:returns the area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class """

    def __init__(self, size):
        """
        Square constructor
        :param size: size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
