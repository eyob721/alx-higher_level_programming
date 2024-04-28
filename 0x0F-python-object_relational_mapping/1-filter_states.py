#!/usr/bin/python3
"""Task 1 - MySQLdb

Description:
    The mysql username, mysql password and mysql database name must be
    passed as argumnets to the script
    Usage: ./1-filter_states.py username password database

"""
from sys import argv

import MySQLdb

if __name__ == "__main__":

    connection_arguments = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],  # mysql username
        "password": argv[2],  # mysql password
        "database": argv[3],  # mysql database name
    }

    with MySQLdb.connect(**connection_arguments) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
        )
        record = cursor.fetchall()
        for rec in record:
            print(rec)
