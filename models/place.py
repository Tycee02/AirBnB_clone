#!/usr/bin/python3
"""place.py"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The class Place inherit from Basemodel
    """

    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    numbe_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        Initializing with args and kwargs
        """
        super().__init__(*args, **kwargs)
