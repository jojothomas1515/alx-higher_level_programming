#!/usr/bin/python3

"""Relationship model."""

from relationship_state import State, Base, relationship
from sqlalchemy import ForeignKey, Column, String, Integer


class City(Base):
    """Class mapper for cities table."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    state = relationship(State, back_populates="cities")
