#!/usr/bin/python3
"""amenity.py"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    The class Amenity inherit from Basemodel
    """

    name = ''

    def __init__.(self. *args, **kwargs):
        """
        Initialing with args and kwargs
        """

        super().__init__(*args, **kwargs)
        if 'name' in kwargs:
            self.name = ['name']
        