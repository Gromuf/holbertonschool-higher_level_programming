#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
all cities along with their corresponding state names
from the `hbtn_0e_4_usa` database. The results are sorted
in ascending order by `cities.id`.
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """

    cursor.execute(request)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
