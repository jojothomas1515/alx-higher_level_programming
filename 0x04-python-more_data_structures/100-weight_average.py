#!/usr/bin/python3

def weight_average(my_list=[]):
    t_score: int = 0
    w_sum: int = 0

    if my_list is None or len(my_list) == 0:
        return (0)

    for s, w in my_list:
        t_score += s*w
        w_sum += w

    return (t_score / w_sum)
