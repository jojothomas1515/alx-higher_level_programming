#!/usr/bin/python3

""" append and write """


def append_write(filename="", text=""):
    """
    append to file
    :param filename: filename
    :param text: text to write
    """

    counts = 0
    with open(filename, 'a', encoding='utf-8') as mf:
        counts = mf.write(text)

    return counts

