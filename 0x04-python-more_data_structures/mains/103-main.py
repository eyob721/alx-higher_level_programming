#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL("./libPython.so")
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]

print("Test 1")
s = b"Hello"
lib.print_python_bytes(s)
print()

print("Test 2")
b = b"\xff\xf8\x00\x00\x00\x00\x00\x00"
lib.print_python_bytes(b)
print()

print("Test 3")
b = b"What does the 'b' character do in front of a string literal?"
lib.print_python_bytes(b)
print()

print("Test 4")
lt = [b"Hello", b"World"]
lib.print_python_list(lt)
print()

print("Test 5")
del lt[1]
lib.print_python_list(lt)
print()

print("Test 6")
lt = lt + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(lt)
print()

print("Test 7")
lt = []
lib.print_python_list(lt)
print()

print("Test 8")
lt.append(0)
lib.print_python_list(lt)
print()

print("Test 9")
lt.append(1)
lt.append(2)
lt.append(3)
lt.append(4)
lib.print_python_list(lt)
print()

print("Test 10")
lt.pop()
lib.print_python_list(lt)
print()

print("Test 11")
lt = ["Holberton"]
lib.print_python_list(lt)
lib.print_python_bytes(lt)
print()
