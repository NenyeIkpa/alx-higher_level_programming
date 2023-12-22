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
    cur.execute("SELECT * FROM cities as c \
                INNER JOIN states as s \
                   ON c.state_id = s.id \
                ORDER BY c.id")
    print(
            ", ". join(
                [cty[2] for cty in cur.fetchall() if cty[4] == state_name])
            )
    cur.close()
    db.close()


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    list_states(user, password, db, state_name)
