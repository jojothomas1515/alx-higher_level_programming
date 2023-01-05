#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argnum = len(argv) - 1
    print("{} argument{}{}".format(argnum,
                                   "s" if argnum > 1 else "",
                                   ":" if argnum > 0 else "."))
    for i in range(argnum):
        print("{}: {}".format(i + 1, argv[i + 1]))
