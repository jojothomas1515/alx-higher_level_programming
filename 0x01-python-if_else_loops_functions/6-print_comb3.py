#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i == 9 and j == 9:
            print("{}{}".format(i, j), end="")
            break
        print("{}{}".format(i, j), end=", ")
