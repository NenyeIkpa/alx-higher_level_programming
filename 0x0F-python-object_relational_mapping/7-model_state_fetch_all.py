#!/usr/bin/python3

""" Select states module """

import sys
import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_states(username, password, db):
    """ lists all states """
    # Connecting to a database using sqlalchemy:
    # step one - create engine
    # the create_engine object accepts a connection string. The connecion which
    # provides info about the data source has the general format:
    # dialect+driver://username:password@host:port/database
    # Connecting to MySQL server at localhost using mysql-python DBAPI
    connection_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, db)
    engine = create_engine(connection_url)

    # step two - create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    all_states = session.query(states).order_by(states.id).all()
    for state in all_states:
        print("({},'{}')".format(state.id, state.name))

if __name__ == "__main__":
    username, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db);
