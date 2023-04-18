#!/usr/bin/python3

"""Relationship state."""

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class mapper for states table."""

    __tablename__ = 'states'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    city = relationship("City", back_populates="state", cascade="all, delete",
                        passive_deletes=True)