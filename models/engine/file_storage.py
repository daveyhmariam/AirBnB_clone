#!/usr/bin/python3
"""Storage engine to store objects into files
"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import json
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances:
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """return all stored obejcts
        Returns:
            dictionary: returns __objects
        """
        return (type(self).__objects)

    def new(self, obj):
        """adds new object

        Args:
            obj (instance of class):
        """
        if obj is not None:
            key = str(type(obj).__name__) + "." + str(obj.id)
            type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        dict = {}

        for key, value in type(self).__objects.items():
            dict[key] = value.to_dict()
        with open(type(self).__file_path, "w") as file:
            json.dump(dict, file, indent=4)

    def reload(self):
        """
        The `reload` function reads data from a file
        and creates objects based on the data.
        """
        try:
            with open(type(self).__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    type(self).__objects[key] = globals()[
                        value["__class__"]](**value)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
