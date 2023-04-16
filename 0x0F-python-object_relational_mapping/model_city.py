#!/usr/bin/python3

"""orm."""

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """States table."""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates='cities')
