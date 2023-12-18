#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb


def list_states(user, password, db, state_name):
    """list all states using MySQLdb """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=password,
            db=db)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id WHERE \
            states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()


if __name__ == "__main__":
    user, password, db, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_states(user, password, db, state_name)
