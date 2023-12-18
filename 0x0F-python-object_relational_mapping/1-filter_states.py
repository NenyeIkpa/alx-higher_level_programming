#!/usr/bin/python3

""" Select states module """

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
    cur.execute("SELECT * FROM states WHERE REGEXP_LIKE(name, '^N', 'c') \
            ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(user, password, db)
