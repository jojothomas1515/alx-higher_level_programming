#!/usr/bin/python3

""" is kind of a class"""


def is_kind_of_class(obj: object, a_class):
    """
    check if object is instance of a class or
    instance of subclass

    :param obj: class instance/object
    :param a_class: class to compare
    :return: True or False
    """

    return isinstance(obj, a_class)
