#!/usr/bin/python3

""" A  function that returns True if the object is
exactly an instance of the specified class ; otherwise False.
 """


def is_same_class(obj, a_class):
    """
    check if it instance of the same class

    :param obj: target object
    :param a_class: Class
    :return: True or false
    """
    return obj.__class__ == a_class
