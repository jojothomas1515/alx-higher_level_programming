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

if __name__ == '__main__':
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))