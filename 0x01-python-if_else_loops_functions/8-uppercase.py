#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 0x61 and ord(str[i]) <= 0x7a:
            print("{}".format(chr(ord(str[i])-0x20)),
                  end='{}'.format("" if i+1 < len(str) else "\n"))
            continue
        print(str[i], end='{}'.format("" if i+1 < len(str) else "\n"))
