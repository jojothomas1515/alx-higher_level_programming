#!/usr/bin/python3

"""json string"""
import json


def from_json_string(my_str):
    """
    from json string
    :param my_str: the string
    :return: python object
    """

    return json.loads(my_str)
