#!/usr/bin/python3

""" SQLInjection  module """

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
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1] == state_name]
    cur.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = '{}'.format(sys.argv[4])
    list_states(user, password, db, state_name)
