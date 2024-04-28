#!/usr/bin/python3
"""Task 5 - MySQLdb

Description:
    The script takes 4 arguments: The mysql username, mysql password, mysql
    database name and state name, and it SQL Injection safe
    Usage: ./5-filter_cities.py username password database state

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
        state_name = argv[4].split(";", 1)[0].strip("\"'")
        cursor.execute(
            """ SELECT cities.name
                FROM cities
                INNER JOIN states ON states.id=cities.state_id
                WHERE states.name LIKE BINARY '{}'
                ORDER BY cities.id ASC;
            """.format(
                state_name
            )
        )
        record = cursor.fetchall()
        print(", ".join([rec[0] for rec in record]))
