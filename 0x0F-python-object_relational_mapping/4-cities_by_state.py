#!/usr/bin/python3
"""Task 4 - MySQLdb

Description:
    The script takes 3 arguments: The mysql username, mysql password, and
    mysql database name
    Usage: ./4-cities_by_state.py username password database

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
            """ SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON states.id=cities.state_id
                ORDER BY cities.id ASC;
            """
        )
        record = cursor.fetchall()
        for rec in record:
            print(rec)
