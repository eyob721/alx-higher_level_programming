#!/usr/bin/python3
"""Task 8"""


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: a function
        *args: variable arguments for `fct`

    Returns:
        - If no exception is raised, the result of `fct`, otherwise None.

    """
    import sys

    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        res = None
    return res
