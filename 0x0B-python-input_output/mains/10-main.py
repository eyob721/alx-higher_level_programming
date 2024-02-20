#!/usr/bin/python3
"""Task 10"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Student = __import__("10-student").Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_0 = student_1.to_json(["first_name", None])
j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(["first_name", "age"])
j_student_3 = student_2.to_json(["middle_name", "age"])

print(j_student_0)
print(j_student_1)
print(j_student_2)
print(j_student_3)
