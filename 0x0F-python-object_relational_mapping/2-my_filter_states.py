#!/usr/bin/python3

""" Search for a state  module """

import sys
import MySQLdb


def list_states(user, password, db, state):
    """list all states using MySQLdb """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=password,
            db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name \
            LIKE BINARY '{}' ORDER BY id ASC".format(state))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3],
    state = sys.argv[4]
    list_states(user, password, db, state)
