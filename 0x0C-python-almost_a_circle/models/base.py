#!/usr/bin/python3

""" Base Class Module"""
import json


class Base:
    """
    Base class to be inherited from

    cvar:
        __nb_objects: private class attribute that counts the
        number of class instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base class constructor

        Args:
            id (int): instance id
        Description:
            if id is not None, set the instance public attr id to
            the passed id value.
            If id i none , increment __nb_objects and set it value to id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list of dict to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        filename = "{}.json".format(cls.__name__)
        li = []
        for i in list_objs:
            li.append(i.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """method returns the list of the JSON string representation

        Args:
            json_string (str): json string representation of a list

        Returns:A list
        """

        if json_string is None or json_string == "":
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new class instance

        Args:
            dictionary: dictionary of needed parameters
        Returns: a new instance
        """
        new: object
        if cls.__name__ == "Rectangle":
            new = cls(1, 2)
        elif cls.__name__ == "Square":
            new = cls(1)

        new.update(**dictionary)

        return new

    @classmethod
    def load_from_file(cls):
        filename: str = "{}.json".format(cls.__name__)

        n_str: str = ""
        obj_li: list = list()

        try:
            with open(filename, "r", encoding="utf-8") as f:
                n_str = f.read()
        except Exception as e:
            return list()

        li_dict = cls.from_json_string(n_str)

        for i in li_dict:
            obj_li.append(cls.create(**i))

        return obj_li
