#!/usr/bin/python

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


if __name__ == '__main__':
    m_list = [1, 2, 3, 0, 5, 6]
    m_list_2 = [1, 2, "jojo", 4, 5, 6, 7]

    new_list = list_division(m_list, m_list_2, 7)
    print(new_list)
