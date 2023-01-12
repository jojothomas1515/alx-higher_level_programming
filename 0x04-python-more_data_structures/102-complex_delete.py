#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    k_list: list = []
    if a_dictionary is None or len(a_dictionary) == 0:
        return (a_dictionary)

    if value == "" or value is None:
        return (a_dictionary)

    for k, v in a_dictionary.items():
        if v == value and type(v) != list:
            k_list.append(k)
    for k in k_list:
        del a_dictionary[k]
    return (a_dictionary)


if __name__ == '__main__':

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print(a_dictionary)
    print("--")
    print(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print(a_dictionary)
    print("--")
    print(new_dict)
