#!/usr/bin/python3

""" IO module"""


def read_file(filename=""):
    """
    open,  read and print to the stdout
    :param filename: name of the file to print in the filesystem
    """
    with open(filename, encoding="utf-8") as r:
        for i in r:
            print(r.readline())
        r.close()


if __name__ == '__main__':
    read_file("0-read_file.py")
