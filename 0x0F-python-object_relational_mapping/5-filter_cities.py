#!/usr/bin/python3
"""
This script takes 4 arguments

    Arguments:
        - mysql username
        - mysql password
        - database name
        - state name

    Description:
        - It lists all the `cities` that belong in the given state name.
        - Given database name is assumed to be `hbtn_0e_0_usa` and that it
          has a table named `cities`. Arguments are not validated.
"""
import sys

import MySQLdb

if __name__ == "__main__":

    def print_result(res):
        """Prints the result"""
        res_len = len(res)
        for i in range(res_len):
            print(result[i][0], end="")
            if i + 1 != res_len:
                print(", ", end="")
        print()

    conn = None
    parameters = {
        "host": "localhost",
        "port": 3306,
        "user": sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
    }
    # SQL Injection safe state name
    state_name = sys.argv[4].split(";", 1)[0].strip("'\"")

    try:
        conn = MySQLdb.connect(**parameters)
        cursor = conn.cursor()
        sql_query = """
            SELECT name
            FROM cities
            WHERE state_id = (
                SELECT id
                FROM states
                WHERE name LIKE BINARY '{}'
            )""".format(
            state_name
        )
        cursor.execute(sql_query)
        result = cursor.fetchall()
        print_result(result)
    finally:
        if conn is not None and conn.open:
            cursor.close()
            conn.close()
