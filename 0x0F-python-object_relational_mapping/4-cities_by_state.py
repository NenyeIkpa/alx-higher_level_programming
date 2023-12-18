#!/usr/bin/python3

""" Lists all cities from given db """

import sys
import MySQLdb


def list_states(user, password, db):
    """list all states using MySQLdb """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=password,
            db=db)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON state_id=states.id ORDER BY cities.id""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    list_states(user, password, db)
