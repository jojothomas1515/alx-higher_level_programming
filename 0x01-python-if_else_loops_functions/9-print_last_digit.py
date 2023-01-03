#!/usr/bin/python3
def print_last_digit(number):
    l_value = (number % 10) if number >= 0 else -(abs(number) % 10)
    print("{:d}".format(l_value), end="")
    return (l_value)
