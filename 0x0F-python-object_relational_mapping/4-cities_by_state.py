#!/usr/bin/python3

""" Select cities module """

import sys
import MySQLdb


def list_cities(user, password, db):
    """list all cities using MySQLdb """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=password,
            db=db)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                   JOIN states\
                   ON cities.state_id = states.id\
                   ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()


if __name__ == "__main__":
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(user, password, db)
