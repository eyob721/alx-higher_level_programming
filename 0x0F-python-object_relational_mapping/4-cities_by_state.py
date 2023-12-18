#!/usr/bin/python3
"""
This script takes 3 arguments

    Arguments:
        - mysql username
        - mysql password
        - database name

    Description:
        - It lists all the `cities` with their corresponding states from the
          database `hbtn_0e_4_usa`.
        - Given database name is assumed to be `hbtn_0e_0_usa` and that it
          has a table named `cities`. Arguments are not validated.
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
        sql_query = """
            SELECT cities.id, cities.name, states.name
            FROM states JOIN cities ON states.id = cities.state_id
            ORDER BY id
            """
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    finally:
        if conn is not None and conn.open:
            cursor.close()
            conn.close()
