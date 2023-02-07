#!/usr/bin/python3

"""Custom List Module"""


class MyList(list):
    """
    Custom List class created by jojo thomas
    """

    def __init__(self, *args, **kwargs):
        """
        Class Constructor

        :param args: args pass
        :param kwargs: kwargs passed
        """
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Print sorted version of my list"""
        result = self.copy()
        result.sort()
        print(result)


if __name__ == "__main__":
    ml = MyList()
    ml.append(1)
    ml.append(3)
    ml.append(2)
    ml.append(4)
    ml.print_sorted()
    print(ml)
