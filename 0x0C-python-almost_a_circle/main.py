#!/usr/bin/python3

""" Main Module """

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

if __name__ == "__main__":
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
