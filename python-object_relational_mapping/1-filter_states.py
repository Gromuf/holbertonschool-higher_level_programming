#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>

- Connects to a MySQL server running on localhost at port 3306.
- Retrieves states from the 'states' table with names starting with 'N'.
- Results are sorted in ascending order by `states.id`.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # MySQL connection parameters
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=passwd,
                         db=db_name)
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
