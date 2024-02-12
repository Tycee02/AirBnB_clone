#!/usr/bin/python3
"""state.py"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    The state class inherit from Basemodel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize the user with *args and **kwargs
        """
        super().__init__(*args, **kwargs)
