#!/usr/bin/python3

"""is subclass module"""


def inherits_from(obj, a_class):
    """
    checks if it a subclass

    :param obj: class instance/object
    :param a_class: class to compare
    :return: True or False
    """

    return issubclass(obj, a_class)
