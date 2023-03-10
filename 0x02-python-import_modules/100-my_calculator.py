#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    import calculator_1 as cl
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == '+':
        print("{} {} {} = {}".format(a, operator, b, cl.add(a, b)))
    elif operator == '-':
        print("{} {} {} = {}".format(a, operator, b, cl.sub(a, b)))
    elif operator == '*':
        print("{} {} {} = {}".format(a, operator, b, cl.mul(a, b)))
    elif operator == '/':
        print("{} {} {} = {}".format(a, operator, b, cl.div(a, b)))
