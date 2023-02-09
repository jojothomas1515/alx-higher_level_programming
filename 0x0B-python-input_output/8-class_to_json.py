#!/usr/bin/python3

"""Class to json"""


def class_to_json(obj):
    """Convert class to serializable json object

    :param obj: the class object to serialize
    """
    return (obj.__dict__)
