#!/usr/bin/python3

""" Rectangle Module"""

from base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width: int, height: int, x: int = 0, y: int = 0, id=None):
        """Rectangle class constructor

        Args:
            width: width of the rectangle.
            height: height of the rectangle
            x: x
            y: y
        """
        width = width
        height = height
        x = x
        y = y
        super().__init__(id)

        @property
        def width(self):
            """getter for the width private variable """
            return self.__width

        @width.setter
        def width(self, width):
            """setter for the width private variable"""
            self.__width = width

        @property
        def height(self):
            """getter for the height private variable"""
            return self.__height

        @height.setter
        def height(self, height):
            """setter for the height private variable"""
            self.__height = height

        @property
        def x(self):
            """getter for the private variable x"""
            return self.__x

        @x.setter
        def x(self, x):
            """setter for the private variable x"""
            self.__x = x

        @property
        def y(self):
            """getter for the private variable y"""
            return self.__y

        @y.setter
        def y(self, y):
            """setter for the private variable y"""
            self.__y = y
