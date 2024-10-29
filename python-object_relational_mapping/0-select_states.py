#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves
all states sorted by id in ascending order.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Connects to a MySQL server running on localhost at port 3306.
    Takes three arguments: mysql username, mysql password, and database name.
    Executes a query to fetch all states from the database, sorted by id,
    and prints each row.
    """

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
