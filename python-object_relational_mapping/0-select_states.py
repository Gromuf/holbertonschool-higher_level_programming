#!/usr/bin/python3
"""
A script that lists all states from the hbtn_0e_0_usa database.

This script connects to a MySQL database and retrieves all records
from the states table, sorted by id in ascending order. The database
credentials (username, password, and database name) are provided as
command line arguments.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
