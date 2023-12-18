#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb


def list_states(user, password, db, state_name_to_search):
    """list all states using MySQLdb """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=user,
            passwd=password,
            db=db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' \
            ORDER BY id ASC".format(state_name_to_search))
    states = cur.fetchall()
    for state in states:
        if state is state_name_to_search:
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3],
    state_to_search = sys.argv[4]
    list_states(user, password, db, state_to_search)
