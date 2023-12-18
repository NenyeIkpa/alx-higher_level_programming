#!/usr/bin/python3

""" Select states module """

import MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Connecting to a database using sqlalchemy:
# step one - create engine
# the create_engine object accepts a connection string. The connecion which
# provides info about the data source has the general format:
# dialect+driver://username:password@host:port/database
# Connecting to MySQL server at localhost using mysql-python DBAPI
engine = create_engine("mysql+mysqldb://root:pass@localhost:3306/hbtn_0e_0_usa")

# step two - connect to the database
# using the connect method of the engine object
# engine.connect()
session = Session(bind=engine)
# print(engine)
session.query(states).order_by(states.id).all()
