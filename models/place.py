#!/usr/bin/python3
"""place.py"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    The class Place inherit from Basemodel
    """

    city_id = ''
    user_id = ''
    description = ''
    number_rooms = 0
    numbe_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''

    def __init__(self, *args, **kwargs):
        """
        Initializing with args and kwargs
        """
        super().__init__(*args, **kwargs)
        if 'city_id' in kwargs:
            self.city_id = kwargs['city_id']
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        if 'desciption' in kwargs:
            self.description = kwargs['description']
        if 'number_rooms' in kwargs:
            self.number_rooms = kwargs['number_room']
        if 'number_bathrooms' in kwargs:
            self.number_bathrooms = kwargs['number_bathrooms']
        if 'max_guest' in kwargs:
            self.max_guest = kwargs['max_guest']
        if 'price_by_night' in kwargs:
            self.price_by_night = kwargs['price_by_night']
        if 'latitude' in kwargs:
            self.latitude = kwargs['latitude']
        if 'longitude' in kwargs:
            self.longitude = kwargs['longitude']
        if 'amenity_ids' in kwargs:
            self.amenity_ids = kwargs['amenity_ids']
        