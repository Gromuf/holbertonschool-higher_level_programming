#!/usr/bin/python3
"""
This module defines the State class that maps to the MySQL table `states`.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from SQLAlchemy Base.
    - Maps to the MySQL table `states`.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
