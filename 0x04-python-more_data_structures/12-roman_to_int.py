#!/usr/bin/python3
def roman_to_int(roman_string):
    """A function that converts a Roman numeral to an integer.

    Args:
        roman_string: given roman numeral in string format

    Returns:
        - converted integer
        - If the `roman_string` is not a string or None, it returns 0

    Description:
        - In the cases of subtractive form, which are the cases of IV, IX, XC,
          XL, CD, or CM. In this cases the value of the first roman numeral is
          subtracted from the value of the second numeral.
          (e.g. IX = 10 - 1 = 9)

    """
    roman_integer = 0
    conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    if type(roman_string) is str:
        prev_int = -1  # -1, a non roman numeral number
        for ch in roman_string:
            cur_int = conversion.get(ch, 0)
            in_subtractive_form = (
                cur_int // prev_int == 5 or cur_int // prev_int == 10
            )
            if in_subtractive_form:
                cur_int -= prev_int * 2  # 2 because prev_int is added already
            prev_int = cur_int
            roman_integer += cur_int
    return roman_integer
