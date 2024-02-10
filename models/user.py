#!/usr/bin/python3
"""user.py"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class represents the users
    and inherits from the BaseModel cass.
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        Initialize the User with *args and **kwargs
        """

        super().__init__(*args, **kwargs)
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'password' in kwargs:
            self.password = kwargs['password']
        if first_name in kwargs:
            self.first_name = kwargs['first_name']
        if last_name in kwargs:
            self.last_name = kwargs['last_name']
