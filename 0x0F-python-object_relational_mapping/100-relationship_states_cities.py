#!/usr/bin/python3

"""Prints Out table info."""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_city import City, Base
from relationship_state import State
import sys

engine = create_engine("mysql+mysqldb://{}")
if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.append(city)
    session.add(state)
    session.add(city)
    session.commit()
