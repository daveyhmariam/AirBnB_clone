#!/usr/bin/python3
"""Storage engine to store objects into files
"""
import json


class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances:
    """
    __objects = {}
    __file_path = "../../file.json"

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
            key = str(type(self).__name__) + str(obj.id)
            type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(type(self).__file, "w") as file:
            json.dump(type(self).__objects, file)

    def reload(self):
        """deserializes the JSON file to __objects
           (only if the JSON file (__file_path) exists
        """
        try:
            with open(type(self), "r") as file:
                type(self).__objects = json.load(file)
        except FileNotFoundError:
            return ({})
