#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list: list = []
    list_len: int = 0
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i]/my_list_2[i])
            list_len += 1
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by zero")
        except IndexError:
            print("out of range")
        finally:
            if list_len - 1 != i:
                new_list.append(0)

    return (new_list)

