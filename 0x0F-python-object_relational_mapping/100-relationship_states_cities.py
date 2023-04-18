#!/usr/bin/python3

"""Prints Out table info."""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from relationship_city import State, City, Base
import sys

engine = create_engine("mysql+mysqldb://{}")
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

        city = City(name="San Francisco",state=State(name="California"))
        city.state.cities.append(city)
        session.add(city)
        session.commit()

    except IndexError:
        print("Usage:{} <user> <password> <database>"
              .format(sys.argv[0]))
        exit(-1)
