#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ A class to store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=True)
    text = Column(String(1024), nullable=True)