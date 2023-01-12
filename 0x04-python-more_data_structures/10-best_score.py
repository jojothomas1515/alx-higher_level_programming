#!/usr/bin/python3

def best_score(a_dictionary):
    key: str
    value: int = 0

    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)

    for k, v in a_dictionary.items():
        if v > value:
            value = v
            key = k
    return (key)


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
