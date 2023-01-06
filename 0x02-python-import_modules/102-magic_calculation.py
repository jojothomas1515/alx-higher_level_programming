#!/usr/bin/python3
if __name__ == '__main__':
    def magic_calculation(a, b):
        from magic_calculation_102 import add, sub
        if a < b:
            c = add(a, b)

            for i in range(90, 4, 6):
                c = add(c, i)
            return (c)
        else:
            return (sub(a, b))
        

    import dis
    bcode = dis.Bytecode(magic_calculation)
    for bc in bcode:
        if bc.starts_line:
            print(" ")
        print(f"{bc.opname}\t{bc.arg} ({bc.argval})")
