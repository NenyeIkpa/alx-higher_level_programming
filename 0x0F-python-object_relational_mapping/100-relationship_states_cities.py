#!/usr/bin/python3
""" List all state objects with sqlalchemy """

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()
