#!/usr/bin/python3
"""
This script takes 3 arguments

    Arguments:
        - mysql username
        - mysql password
        - database name

    Description:
        - It lists all states that start with the `N` (upper N).
        - Database name is assumed to be `hbtn_0c_0_usa` and that it has a
          table named `states`. Arguments are not validated.
"""
import sys

import MySQLdb

if __name__ == "__main__":
    conn = None
    parameters = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
    }
    try:
        conn = MySQLdb.connect(**parameters)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name like binary 'N%' ORDER BY id"
        )
        result = cursor.fetchall()
        for row in result:
            print(row)
    finally:
        if conn is not None and conn.open:
            cursor.close()
            conn.close()
