#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    A function that converts a Roman numeral to an integer

    Args:
        roman_string: given roman numeral in string format

    Returns:
        - converted integer
        - If the `roman_string` is not a string or None, it returns 0

    """
    integer = 0
    conversion = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str:
        prev = ''
        for ch in roman_string:
            roman_int = conversion.get(ch, 0)
            if ch != 'I' and prev == 'I':
                roman_int -= 2  # -2 beacause 'I' is already added
            prev = ch
            integer += roman_int
    return integer
