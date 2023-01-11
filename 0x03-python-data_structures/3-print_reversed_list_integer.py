#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))


if __name__ == '__main__':
    my_list = [x for x in range(30)]
    print_reversed_list_integer(my_list)
