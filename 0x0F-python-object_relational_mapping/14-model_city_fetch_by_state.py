#!/usr/bin/python3
"""Print all state."""

import sys

from model_state import State
from model_city import City, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]))
        Base.metadata.create_all(engine)

        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        states = session.query(State).order_by(City.id).all()
        if len(state) != 0:
            for state in states:
                print("{}: ({}) {}".format(state.name,
                                           state.id, state.city.name))
        else:
            print("Nothing")
    except IndexError:
        print("Usage:{} <user> <password> <database>"
              .format(sys.argv[0]))
        exit(-1)
