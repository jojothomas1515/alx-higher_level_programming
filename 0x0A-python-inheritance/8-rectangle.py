#!/usr/bin/python3

"""Base Geometry Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


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
