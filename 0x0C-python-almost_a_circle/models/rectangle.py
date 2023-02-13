#!/usr/bin/python3

""" Rectangle Module"""

from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width: int,
                 height: int, x: int = 0, y: int = 0, id=None):
        """Rectangle class constructor

        Args:
            width: width of the rectangle.
            height: height of the rectangle
            x: x
            y: y
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the width private variable """
        return self.__width

    @width.setter
    def width(self, value: int):
        """setter for the width private variable

        Args:
            value (int): value to set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height private variable"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """setter for the height private variable

        Args:
            value (int): value to set height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the private variable x"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """setter for the private variable x
        Args:
            value (int): value to set x
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the private variable y"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """setter for the private variable y

        Args:
            value (int): value to set y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes and return the area for rectangle
        which formula is A = W * L
        where w stands for width and l stands for length/height

        Returns:
            the area or a rectangle
        """

        return self.width * self.height

    def display(self):
        """visual representation of the rectangle in the terminal"""
        my_str = "{}{}".format(" " * self.x, "#" * self.width)
        print("\n" * self.y, end="")
        print((my_str + "\n") * self.height, end="")

    def update(self, *args, **kwargs):
        """Updates the Rectangle instance attributes

        Args:
            args: non keyword positional arguments to be set in this
            order => id, width, height, x, y
            kwargs: keyword argument only usable if args is None and
            to be set if the corresponding instance attributes exist
        """
        al = len(args)

        if al == 0:
            for k in kwargs:
                if k == "id":
                    self.id = kwargs["id"]
                elif k == "width":
                    self.width = kwargs["width"]
                elif k == "height":
                    self.height = kwargs["height"]
                elif k == "x":
                    self.x = kwargs["x"]
                elif k == "y":
                    self.y = kwargs["y"]

        if al > 0:
            self.id = args[0]
        if al > 1:
            self.width = args[1]
        if al > 2:
            self.height = args[2]
        if al > 3:
            self.x = args[3]
        if al > 4:
            self.y = args[4]

    def to_dictionary(self):
        """Convert Rectangle attributes to dictionary"""
        return dict(id=self.id, width=self.width, height=self.height,
                    x=self.x, y=self.y)

    def __str__(self):
        """string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
