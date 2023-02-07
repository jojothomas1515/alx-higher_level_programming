#!/usr/bin/python3

""" append and write """


def append_write(filename="", text=""):
    """
    append to file
    :param filename: filename
    :param text: text to write
    """

    with open(filename, 'a', 'utf-8') as mf:
        mf.write(text)
