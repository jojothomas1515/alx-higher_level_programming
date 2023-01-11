#!/usr/bin/python3

from hmac import new


def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None and type(a_dictionary) == dict:
        a_dictionary[key] = value
        return a_dictionary
    else:
        new_dictionary = dict()
        new_dictionary[key] = value
        return new_dictionary
