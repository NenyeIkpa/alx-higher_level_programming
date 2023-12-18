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
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        if state is state_name_to_search:
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    user, password, db, state_name_searched =  sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_states(user, password, db, state_name_searched)
