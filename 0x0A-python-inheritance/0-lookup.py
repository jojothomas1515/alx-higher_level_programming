#!/usr/bin/python3

""" Look Up Module"""


def lookup(clss: object):
    """
    function that returns the list of available attributes
    and methods of an object

    Args:
        clss: this is the passed arguments
    return: returns a list of available arguments
    """
    return dir(clss)
