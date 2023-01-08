#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Searh for the largest integer in a list

    this function has a time complesity of O(n)

    Parameters:
        my_list: Target list to search through
    return: max/largest value.
    """

    if len(my_list) == 0:
        return (None)

    my_max: int = 0

    for i in my_list:
        if my_max == 0:
            my_max = i
        if i > my_max:
            my_max = i

    return (my_max)


if __name__ == '__main__':
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
