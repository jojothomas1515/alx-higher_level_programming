#!/usr/bin/python3

""" append and write """


def append_write(filename="", text=""):
    """"""

    with open(file=filename, mode='a', encoding='utf-8') as mf:
        mf.write(text)
