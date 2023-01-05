#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4 as hid
    for i in dir(hid):
        if i.startswith('__'):
            continue
        print(i)
