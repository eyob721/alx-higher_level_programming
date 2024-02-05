#!/usr/bin/python3
"""Task 4"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1: list 1
        my_list_2: list 2

    Returns:
        - A list contain the result of the division.

    NOTE:
        - If an exception is raised a value of 0 is used in the result list.

    """
    i = 0
    res_lst = []
    while i < list_length:
        try:
            res = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            res_lst.append(res)
        i += 1
    return res_lst
