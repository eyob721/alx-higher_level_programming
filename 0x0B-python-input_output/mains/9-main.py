#!/usr/bin/python3
"""Task 9"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Student = __import__("9-student").Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student["first_name"])
    print(type(j_student["first_name"]))
    print(j_student["age"])
    print(type(j_student["age"]))
