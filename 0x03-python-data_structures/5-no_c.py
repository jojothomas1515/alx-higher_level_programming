#!/usr/bin/python3
def no_c(my_string: str):
    new_str = ""
    for c in my_string:
        if c in 'cC':
            continue
        new_str = new_str + c

    return (new_str)


if __name__ == '__main__':
    text = "call craCCck cin"
    print(no_c(text))
