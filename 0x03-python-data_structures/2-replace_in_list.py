#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)


if __name__ == '__main__':
    my_list = [x + 1 for x in range(10)]
    this_list = my_list.copy()
    print(my_list)
    replace_in_list(my_list, 3, 22)
    print(my_list)
    print(this_list)
