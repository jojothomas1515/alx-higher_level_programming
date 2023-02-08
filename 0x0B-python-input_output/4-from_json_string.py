#!/usr/bin/python3
import json

"""json string"""


def from_json_string(my_str):
    """from json string

    :param my_str: the string
    :return: python object
    """

    return json.loads(my_str)
