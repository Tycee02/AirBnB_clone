#!/usr/bin/python3
"""Module containing functions to serialize and deserialize JSON"""
import json

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


class FileStorage:
    """Class to handle the operations of serialization and deserialization
    of JSON
    """

    # Private class attributes
    __file_path = "file.json"  # Path to JSON file
    __objects = {}  # store all objects by <class nam>.id

    def all(self):
        """Method to returns all objects created"""
        return FileStorage.__objects

    def new(self, obj):
        """Method to set new object to storage"""
        if obj is not None:
            # Create the key <obj class name>.id
            key = obj.__class__.__name__ + "." + obj.id
            # Save the object in the Dictionary
            FileStorage.__objects[key] = obj

    def save(self):
        """Method to serialize and save a JSON to file"""
        json_obj = {}
        for key in FileStorage.__objects:
            json_obj[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(json_obj, f)

    def reload(self):
        """Method to deserialize JSON from file"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_obj = json.load(f)

            for key in json_obj:
                # Retrieve the class name from the object
                obj_class = classes[json_obj[key]["__class__"]]
                # Retrive the class Dictionary
                obj_dict = json_obj[key]
                # Create a new Instance of the class using the
                # dictionary
                obj = obj_class(**obj_dict)
                # Add the object to the __objects
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            return
