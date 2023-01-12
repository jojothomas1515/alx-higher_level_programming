#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is None or len(a_dictionary) == 0:
        return (a_dictionary)

    for k, v in a_dictionary.items():
        if v in value:
            del a_dictionary[k]

    return (a_dictionary)
