#!/usr/bin/python3
"""Task 6 - SQLAlchemy

This module contains the definition of the mapped class `State`.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition of State - mapped to table `states`"""

    __tablename__ = "states"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
