#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="places", cascade="delete")
    __tablename__ = "places"

    @property
    def reviews(self):
        """eturns the list of Review instances
        with place_id equals to the current Place.id"""
        from models import storage
        _list = []
        for key in storage.all(Review):
            if self.id == key.place_id:
                _list.append(key)
        return _list

    @property
    def amenities(self):
        """Amenities relation wit place"""
        from models import storage
        _list = []
        for key in storage.all(Review):
            if self.id == key.place_id:
                _list.append(key)
        return _list

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
