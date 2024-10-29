#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all states matching a given name, sorted by id in ascending order.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to a MySQL server running on localhost at port 3306.
    Takes four arguments: mysql username, mysql password, database name,
    and the state name to search for. Executes a query to fetch matching
    states from the database, sorted by id, and prints each result.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    request = ("SELECT * FROM states WHERE BINARY name = '{}' "
               "ORDER BY id ASC;"
               ).format(argv[4])

    cursor.execute(request)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
