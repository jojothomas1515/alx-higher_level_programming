#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is None or key == "":
        return a_dictionary
    elif a_dictionary.get(key) is not None:
        a_dictionary.pop(key)
        return a_dictionary
    return a_dictionary
