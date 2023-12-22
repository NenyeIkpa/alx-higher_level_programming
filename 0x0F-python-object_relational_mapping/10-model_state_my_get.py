#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db, state):
    """ lists all states with a """
    connection_url = "mysql+mysqldb://{}:\
            {}@localhost:3306/{}".format(username, password, db)
    engine = create_engine(connection_url)

    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state_sought = session.query(State).\
            filter(State.name == state).order_by(State.id).one()
        print("{}".format(state_sought.id))
    except Exception:
        print("Not found")


if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    state = sys.argv[4]
    list_states(username, password, db, state)
