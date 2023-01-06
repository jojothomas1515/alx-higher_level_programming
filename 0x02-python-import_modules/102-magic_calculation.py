#!/usr/bin/python3
if __name__ == '__main__':
    def magic_calculation(a, b):
        from calculation_1 import add, sub
        if a < b:
            c = add(a, b)

            for i in range(90):
                c = add(c, i)
            return (c)
        return (sub(a, b))
