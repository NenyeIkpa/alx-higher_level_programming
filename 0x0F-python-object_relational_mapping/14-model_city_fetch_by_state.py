#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


def list_states(username, password, db):
    """ lists all states """
    connection_url = "mysql+mysqldb://{}:\
            {}@localhost:3306/{}".format(username, password, db)
    engine = create_engine(connection_url)

    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all()
    for state, city in all_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))


if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db)
