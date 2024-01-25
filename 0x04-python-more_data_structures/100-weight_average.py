#!/usr/bin/python3
def weight_average(my_list=[]):
    """A function that returns the weighted average of all integers in a list.

    Args:
        - my_list: list of integer tuples in the form (<score>, <weight>)

    Returns:
        - weighted average
        - if my_list is empty or None, it returns 0

    Description:
        - weight average = ∑(score * weight) / ∑(weight)

    """
    avg = 0
    if my_list:
        score_sum = weight_sum = 0
        for int_tup in my_list:
            score, weight = int_tup
            score_sum += score * weight
            weight_sum += weight
        avg = score_sum / weight_sum
    return avg
