#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db):
    """ lists all states """
    connection_url = "mysql+mysqldb://{}:\
            {}@localhost:3306/{}".format(username, password, db)
    engine = create_engine(connection_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()


if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db)
