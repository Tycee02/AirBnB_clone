#!/usr/bin/python3
"""
Base Model class
"""
import models
import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class serves as a base class for other classes, providing common
    attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (str): Unique identifier generated using uuid.uuid4().
            created_at (datetime): Timestamp of the creation time.
            updated_at (datetime): Timestamp of the last update time.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(value, time)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        String representation of the object.

        Returns:
            str: String representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object into a dictionary representation.

        Returns:
            dict: Dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
