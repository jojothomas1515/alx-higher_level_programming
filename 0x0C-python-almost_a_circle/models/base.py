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
