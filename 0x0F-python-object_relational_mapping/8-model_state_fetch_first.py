#!/usr/bin/python3
"""Print all state."""

import sys

from model_state import Base, State
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
        data = session.query(State).first()
        if data:
            print("{}: {}".format(data.id, data.name))
        else:
            print()

    except IndexError as e:
        print("Usage:{} <user> <password> database"
              .format(sys.argv[1]))
        exit(-1)
