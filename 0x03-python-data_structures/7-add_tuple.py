#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()) -> tuple:
    """
    Add tuple.

    parameter:
        tuple_a:
            first tuple
        tuple_b:
            second tuple
    Return: new tuple thats the sum of both tuple
    """
    al = tuple_a[0] if len(tuple_a) > 0 else 0
    ar = tuple_a[1] if len(tuple_a) > 1 else 0
    bl = tuple_b[0] if len(tuple_b) > 0 else 0
    br = tuple_b[1] if len(tuple_b) > 1 else 0
    new_tuple: tuple = (al+bl, ar+br)

    return (new_tuple)


if __name__ == '__main__':

    j: tuple[int, int] = add_tuple((22,), (43, 32))
    print(j)
