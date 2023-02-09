#!/usr/bin/python3

"""is subclass module"""


def inherits_from(obj, a_class):
    """
    checks if it a subclass

    :param obj: class instance/object
    :param a_class: class to compare
    :return: True or False
    """
    if obj.__class__ == a_class:
        return False
    return issubclass(obj.__class__, a_class)
