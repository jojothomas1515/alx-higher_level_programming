#!/usr/bin/python3
from hashlib import new


def uniq_add(my_list=[]):
    new_li = []
    acc: int = 0
    for i in my_list:
        if i not in new_li:
            new_li.append(i)
            acc += i
    return (acc)


if __name__ == '__main__':

    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    # print("Result: {:d}".format(result))
    print(result)
