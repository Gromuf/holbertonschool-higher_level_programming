#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=passwd,
                         db=db_name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
