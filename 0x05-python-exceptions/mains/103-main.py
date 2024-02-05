#!/usr/bin/python3 -u
"""Main script for task 10"""

import ctypes

lib = ctypes.CDLL("./libPython.so")
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]

s = b"Hello"
lib.print_python_bytes(s)
b = b"\xff\xf8\x00\x00\x00\x00\x00\x00"
lib.print_python_bytes(b)
b = b"What does the 'b' character do in front of a string literal?"
lib.print_python_bytes(b)
lt = [b"Hello", b"World"]
lib.print_python_list(lt)
del lt[1]
lib.print_python_list(lt)
lt = lt + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"School", "Betty"]
lib.print_python_list(lt)
lt = []
lib.print_python_list(lt)
lt.append(0)
lib.print_python_list(lt)
lt.append(1)
lt.append(2)
lt.append(3)
lt.append(4)
lib.print_python_list(lt)
lt.pop()
lib.print_python_list(lt)
lt = ["School"]
lib.print_python_list(lt)
lib.print_python_bytes(lt)
f = 3.14
lib.print_python_float(f)
lt = [
    -1.0,
    -0.1,
    0.0,
    1.0,
    3.14,
    3.14159,
    3.14159265,
    3.141592653589791238462643383279502884197169399375105820974944592307816406286,
]
print(lt)
lib.print_python_list(lt)
lib.print_python_float(lt)
lib.print_python_list(f)
