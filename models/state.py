#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """ """
            from models.city import City
            from models import storage
            list_of_city = []
            for i in storage.all(City):
                if storage.all(City)[i].state_id == self.id:
                    list_of_city.append(storage.all(City)[i])
            return list_of_city
