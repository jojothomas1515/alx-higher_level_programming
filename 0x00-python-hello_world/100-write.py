#!/usr/bin/python3
from sys import exit
from os import write
text = f"and that piece of art is useful - Dora Korpar, 2015-10-19"
write(2, text.encode())
exit(1)
