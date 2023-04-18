#!/usr/bin/python3

"""
Write a script that lists all State objects, and corresponding City objects.

contained in the database hbtn_0e_101_usa.

Your script should take 3 arguments: mysql username, mysql password and
 database name
You must use the module SQLAlchemy
The connection to your MySQL server must be to localhost on port 3306
You must only use one query to the database
You must use the cities relationship for all State objects
Results must be sorted in ascending order by states.id and cities.id
Results must be displayed as they are in the example below
Your code should not be executed when imported.
"""

from model_city import City, State, Base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.engine import create_engine
import sys

if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
        print(state.cities)

        # because of the relationship between state and city table
        # we can get all the cities associated with a state
        # for city in state.cities:
        #     print("\t{}: {}".format(city.id, city.name))
