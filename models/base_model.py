#!/usr/bin/python3
"""Base Model class"""

from datetime import datetime
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model
        Argrs:
                *args
        Return:
                None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return the Representation of Object"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """updates the public instance attribute
                updated_at with the current datetime
        Args:
                None
        Return:
                None

        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
                __dict__ of the instance:

        Args:
                None
        Return:
                None

        """
        obj_dict = self.__dict__.copy()
        if "created_at" in obj_dict:
            obj_dict["created_at"] = obj_dict["created_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        if "updated_at" in obj_dict:
            obj_dict["updated_at"] = obj_dict["updated_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
