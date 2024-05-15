#!/usr/bin/python3
"""Task 6 - Test script for task 6, model_state

Note:
    You need to pass the user, password, and database to the script as
    argumnets

"""
import os
import sys

from sqlalchemy import create_engine

# Add module from parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

Base = __import__("model_state").Base
State = __import__("model_state").State

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, database),
    pool_pre_ping=True,
)
Base.metadata.create_all(engine)
