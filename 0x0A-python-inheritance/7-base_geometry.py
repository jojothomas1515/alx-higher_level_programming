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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
