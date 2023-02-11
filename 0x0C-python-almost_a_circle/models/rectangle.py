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
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width