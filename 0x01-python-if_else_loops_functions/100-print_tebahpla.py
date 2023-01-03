#!/usr/bin/python3
for i in reversed(range(0x61, 0x7A+0x1)):
    print("{}".format(chr(i) if i % 0x2 == 0 else chr(i-32)), end='')
