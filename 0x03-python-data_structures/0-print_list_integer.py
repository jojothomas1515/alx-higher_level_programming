#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))


if __name__ == '__main__':
    my_list = [x**2 for x in range(100)]
    print_list_integer(my_list)
