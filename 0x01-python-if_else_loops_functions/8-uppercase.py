#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}".format(chr(ord(str[i])-0x20)
                          if ord(str[i]) >= 0x61 and ord(str[i]) <= 0x7a
                          else chr(ord(str[i]))),
              end="")
    print("")

uppercase("holberton")