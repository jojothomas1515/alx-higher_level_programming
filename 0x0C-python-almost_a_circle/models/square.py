#!/usr/bin/python3

"""Square model class"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class subclassed from rectangle"""

    def __init__(self, size: int, x: int = 0, y: int = 0, id=None):
        """Square class constructor

        Args:
            size: size of the square
            x: x position of the square for display
            y: y position of the square for display
            id: The id the of the square instance (optional)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value: new size value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the square object"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
