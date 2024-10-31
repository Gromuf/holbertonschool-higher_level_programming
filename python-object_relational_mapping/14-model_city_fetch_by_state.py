#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa,
displayed as <state name>: (<city id>) <city name>.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    result = (
        session.query(State, City)
        .filter(State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
