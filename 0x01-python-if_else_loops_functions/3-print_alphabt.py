#!/usr/bin/python3
import string

for c in range(26):
    if chr(c + 0x61) in 'qe':
        continue
    print("{}".format(chr(c + 0x61)), end='')
