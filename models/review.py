#!/usr/bin/python3
"""review.py"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The class Review inherit fom Basemodel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing with args and kwargs
        """
        super().__init__(*args, **kwargs)
