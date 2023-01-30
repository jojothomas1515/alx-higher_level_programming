#!/usr/bin/python3

"""Rectangle class module"""


class Rectangle:
    """Empty rectangle class"""

    def __init__(self, width=0, height=0):
        """Constructor of the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value for width

        Args:
            value (int): new value for width

        """
        if not isinstance(value, int):
            raise (TypeError("width must be an integer"))
        elif (value < 0):
            raise (ValueError("width must be >= 0"))

        self.__width = value

    @property
    def height(self):
        """Returns the value for width"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value for height

        Args:
            value (int): new value for height

        """
        if not isinstance(value, int):
            raise (TypeError("height must be an integer"))
        elif (value < 0):
            raise (ValueError("height must be >= 0"))

        self.__height = value

    def area(self):
        """Returns the area for the rectangle

        Example:
            >>> rect = Rectangle(3,4)

            >>> rect.area()
            12

        """
        return (self.height * self.width)

    def perimeter(self):
        """Returns the perimeter for the rectangle

        Example:
            >>> rect = Rectangle(3,4)
            >>> rect2 = Rectangle(2, 0)

            >>> rect.perimeter()
            14

            >>> rect2.perimeter()
            0

        """
        if self.height == 0 or self.width == 0:
            return (0)
        return (2 * (self.height + self.width))

    def __str__(self):
        """String representation of rectangle instance

        Example:
            >>> rect = Rectangle(3,4)
            >>> rect2 = Rectangle(2, 0)

            >>> print(str(rect))
            ###
            ###
            ###
            ###
            <BLANKLINE>

            >>> print(str(rect2))
            <BLANKLINE>

            >>> print(repr(rect)) # doctest: +ELLIPSIS
            <3-rectangle.Rectangle object at 0x...>

        """
        result_str = ""
        if self.width == 0 or self.height == 0:
            return (result_str)
        for i in range(self.height):
            result_str += "{}{}".format("#"*self.width,
                                        "\n" if i != self.height - 1
                                        else "")

        return result_str

    def __repr__(self):
        """string representation that can be evaluated"""

        return ("Rectangle({:d}, {:d})".format(self.width, self.height))
    
    def __del__(self):
        """Rectangle Destructor"""
        print("Bye rectangle...")
