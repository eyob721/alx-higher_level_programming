#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL("./libPyList.so")
lib.print_python_list_info.argtypes = [ctypes.py_object]
lst = ["hello", "World"]
lib.print_python_list_info(lst)
del lst[1]
lib.print_python_list_info(lst)
lst = lst + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(lst)
lst = []
lib.print_python_list_info(lst)
lst.append(0)
lib.print_python_list_info(lst)
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lib.print_python_list_info(lst)
lst.pop()
lib.print_python_list_info(lst)
