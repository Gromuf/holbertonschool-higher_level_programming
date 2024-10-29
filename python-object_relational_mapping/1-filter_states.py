#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>

- Connects to a MySQL server running on localhost at port 3306.
- Retrieves states from the 'states' table with names starting with 'N'.
- Results are sorted in ascending order by `states.id`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to the MySQL database and retrieves all states
    starting with 'N', sorted by `states.id` in ascending order.
    Prints each matching state to the console.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    cursor.execute(
        """SELECT * FROM states
        WHERE BINARY name LIKE 'N%' ORDER BY id ASC;"""
        )
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
