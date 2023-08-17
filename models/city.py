#!/usr/bin/python3
"""
This script defines the City class, representing a city for a MySQL database.
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Represents a city for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table 'cities'.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
        places (sqlalchemy relationship):
        Relationship with the 'Place' class, cascade delete.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
