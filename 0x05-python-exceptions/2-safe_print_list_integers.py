#!/usr/bin/python3

from multiprocessing.sharedctypes import Value


def safe_print_list_integers(my_list=[], x=0):

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except Exception:
            pass

    print()
