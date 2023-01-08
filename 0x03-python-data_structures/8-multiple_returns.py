#!/usr/bin/python3

def multiple_returns(sentence):
    length: int = len(sentence)
    f_char: str = sentence[0] if length > 0 else None
    return ((length, f_char))


if __name__ == '__main__':
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print(multiple_returns(sentence))
    print("Length: {:d} - First character: {}".format(length, first))
