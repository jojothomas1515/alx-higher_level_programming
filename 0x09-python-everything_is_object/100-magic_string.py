#!/usr/bin/python3
def magic_string():
    return str(", ").join(["BestSchool" for i in range(
        (globals().popitem()[1] + 1))])

for i in range(1):
    print(magic_string())