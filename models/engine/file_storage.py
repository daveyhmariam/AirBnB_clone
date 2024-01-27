'''class that handles object storage'''
import json
from models import base_model

class FileStorage:
    '''The FileStorage class provides methods
    for managing and persisting objects in a file.'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects
        """
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (class_instance): instance of a certain class
                particularly BaseModel or descendants
        """
        if obj != None:
            key = obj.__dict__[__class__] + str(obj.id)
            type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        try:
            with open(type(self).__file_path, "w") as f:
                json.dump(type(self).__objects, f)
        except Exception as e:
            pass

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        try:
            with open(type(self).__file_path, "r") as f:
                type(self).__objects = json.load(f)
        except Exception as e:
            pass
