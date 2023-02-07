#!/usr/bin/python3

"""write file module"""


def write_file(filename="", text=""):
    """
    create a file and write to it or overwrite to it
    if file exist
    :param filename: target file
    :param text: text to be written
    """

    with open(filename, "w", encoding="utf-8") as mf:
        mf.write(text)
