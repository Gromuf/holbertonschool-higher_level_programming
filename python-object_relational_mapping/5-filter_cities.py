#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities
of that state from the database `hbtn_0e_4_usa`,
sorted by `cities.id` in ascending order.
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
    request = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """

    cursor.execute(request, (argv[4],))
    cities = cursor.fetchall()
    result = ", ".join([city[0] for city in cities])

    print(result)

    cursor.close()
    db.close()
