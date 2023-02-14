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

    def update(self, *args, **kwargs):
        """Updates the Square instance attributes

                Args:
                    args: non keyword positional arguments to be set in this
                    order => id, size, x, y
                    kwargs: keyword argument only usable if args is None and
                    to be set if the corresponding instance attributes exist
                """
        al = len(args)

        if al == 0 or args is None:
            for k in kwargs:
                if k == "id":
                    self.id = kwargs["id"]
                elif k == "size":
                    self.size = kwargs["size"]
                elif k == "x":
                    self.x = kwargs["x"]
                elif k == "y":
                    self.y = kwargs["y"]

        if al > 0:
            self.id = args[0]
        if al > 1:
            self.size = args[1]
        if al > 2:
            self.x = args[2]
        if al > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Convert Square attributes to dictionary"""
        return dict(id=self.id, size=self.size,
                    x=self.x, y=self.y)

    def __str__(self):
        """String representation of the square object"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
