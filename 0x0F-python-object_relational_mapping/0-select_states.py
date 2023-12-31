#!/usr/bin/python3
"""
This script takes 3 arguments

    Arguments:
        - mysql username
        - mysql password
        - database name

    Description:
        - It lists all the states in the database
        - Database name is assumed to be `hbtn_0c_0_usa` and that it has a
          table named `states`. Arguments are not validated.
"""
import sys

import MySQLdb

if __name__ == "__main__":
    conn = None
    parameters = {
        "host": "localhost",
        "user": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
        "port": 3306,
    }
    try:
        conn = MySQLdb.connect(**parameters)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id")
        result = cursor.fetchall()
        for row in result:
            print(row)
    finally:
        if conn is not None and conn.open:
            conn.close()
