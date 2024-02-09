#!/usr/bin/python3
"""review.py"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The class Review inherit fom Basemodel
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self. *args, **kwargs):
        """
        Initializing with args and kwargs
        """
        if 'place_id' in kwargs:
            self.place_id = kwargs['place_id']
        if 'user_id' in kwargs:
            self.user_id = kwargs['user_id']
        if 'text' in kwargs:
            self.text = kwargs['text']
        