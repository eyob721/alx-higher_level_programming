#!/usr/bin/python3
"""Task 11"""

import os
import sys

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Student = __import__("11-student").Student
read_file = __import__("0-read_file").read_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if len(sys.argv) != 2:
    print("Usage: ./11-main.py <path_to_json_file>")
    exit(1)

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

# Save a students info to a json file
student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print("-----------------------------")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print(
    "{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age)
)


save_to_json_file(j_student_1, path)
read_file(path)  # Check if the json file is saved
print("\nSaved to disk")
print("-----------------------------")


# Create an arbitary student that will get the attributes of Initial student
print("Fake student:")
print("-----------------------------")
new_student_1 = Student("Fake", "Fake", 89)
print("--- Before ---")
print(new_student_1)
print(type(new_student_1))
print(
    "{} {} {}".format(
        new_student_1.first_name, new_student_1.last_name, new_student_1.age
    )
)
print("--- ---")


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print("--- After ---")
print(new_student_1)
print(type(new_student_1))
print(
    "{} {} {}".format(
        new_student_1.first_name, new_student_1.last_name, new_student_1.age
    )
)
print("--- ---")
print(new_student_1.__dict__)
