#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list) - 1:
        return (None)
    return (my_list[idx])


if __name__ == '__main__':
    my_list = [x + 1 for x in range(10)]
    print(element_at(my_list, 3))
