#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argnum = len(argv) - 1
    result = 0
    for i in range(argnum):
        result += int(argv[i + 1])
    print(result)
