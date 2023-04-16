#!/usr/bin/python3

"""orm."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """States table."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
