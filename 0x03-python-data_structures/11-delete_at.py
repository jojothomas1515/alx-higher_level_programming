#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length: int = len(my_list)

    if length == 0 or idx > length - 1:
        return (my_list)
    del my_list[idx]
    new_list: list = my_list.copy()

    return my_list


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
