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

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
