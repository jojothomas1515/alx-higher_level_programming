#!/usr/bin/python3

"""Peak finder."""


def find_peak(list_of_integers: list):
    """Return the highest number."""
    res = list_of_integers
    len_l = len(res)
    if (len_l == 0):
        return None
    res.sort()
    return res[len_l - 1]

