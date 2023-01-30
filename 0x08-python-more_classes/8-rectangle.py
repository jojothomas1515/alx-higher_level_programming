#!/usr/bin/python3

"""Rectangle class module"""


class Rectangle:
    """Empty rectangle class

    Args:
        number_of_instances (int): num of rectangle instances
        print_symbol (any) : symbol used by the str method
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor of the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            result_str += "{}{}".format(str(self.print_symbol)*self.width,
                                        "\n" if i != self.height - 1
                                        else "")

        return result_str

    def __repr__(self):
        """string representation that can be evaluated"""

        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """Rectangle Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compare two rectangles and return the largest

        Args:
            rect_1 (Rectangle): instance of the Rectangle
            rect_2 (Rectangle): instance of the Rectangle

        Return: the largest of both
        """
        if not isinstance(rect_1, Rectangle):
            raise (TypeError("rect_1 must be an instance of Rectangle"))
        if not isinstance(rect_2, Rectangle):
            raise (TypeError("rect_2 must be an instance of Rectangle"))

        if rect_1.area() == rect_2.area():
            return (rect_1)
        if rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
