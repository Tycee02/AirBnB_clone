#!/usr/bin/python3
"""Base Model class"""

from datetime import datetime
import models
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
        # Create an Instance from a dictionary
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

        if hasattr(self, "created_at") and type(self.created_at) is str:
            self.created_at = datetime.strptime(kwargs["created_at"], time)
        if hasattr(self, "updated_at") and type(self.updated_at) is str:
            self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            # Create a new Instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

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
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
                __dict__ of the instance:

        Args:
                None
        Return:
                None

        """
        # Copy the instance __dict__ to new dictionary
        obj_dict = self.__dict__.copy()
        # Check if the created_at and update_at attrs exists and format the
        # date to ISO format
        if "created_at" in obj_dict:
            obj_dict["created_at"] = obj_dict["created_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        if "updated_at" in obj_dict:
            obj_dict["updated_at"] = obj_dict["updated_at"].strftime(
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        obj_dict["__class__"] = self.__class__.__name__

        # Return the a dictionary with the class name and all attrs
        return obj_dict
