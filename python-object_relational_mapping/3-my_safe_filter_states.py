#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
all rows in the `states` table of `hbtn_0e_0_usa`
where `name` matches the given argument, in a way that is safe
from SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()
    request = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"

    cursor.execute(request, (argv[4],))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
