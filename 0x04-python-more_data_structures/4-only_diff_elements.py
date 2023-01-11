#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    list1 = list(filter(lambda x: x not in set_2, set_1))
    res = list(filter(lambda x: x not in set_1, set_2)) + list1
    return res


if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
