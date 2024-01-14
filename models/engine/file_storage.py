#!/usr/bin/python3
"""
File storage engine for obects to persist data

"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage that serializes instances to a JSON file
          and deserializes JSON file to instances
    """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return (self.__class__.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (instance object):
        """
        obj_name = obj.__class__.__name__ + "." + str(obj.id)
        self.__class__.__objects[obj_name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__class__.__file_path, "w") as file_data:
            json_dict = {}
            for o in self.__class__.__objects:
                json_dict[o] = self.__class__.__objects[o].to_dict()
            json.dump(json_dict, file_data, indent=4)

    def reload(self):
        try:
            with open(self.__class__.__file_path, "r") as file_data:
                json_dict = json.load(file_data)
                for v in json_dict.values():
                    cls_name = v["__class__"]
                    del v["__class__"]
                    self.new(eval(cls_name)(**v))
        except FileNotFoundError:
            pass
