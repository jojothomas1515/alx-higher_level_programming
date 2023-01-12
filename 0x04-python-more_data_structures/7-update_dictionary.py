#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key is None or key == "":
        return (a_dictionary)
    elif a_dictionary is not None and type(a_dictionary) == dict:
        a_dictionary[key] = value
        return a_dictionary
    else:
        new_dictionary = dict()
        new_dictionary[key] = value
        return new_dictionary
