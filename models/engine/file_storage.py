"""class that handles object storage"""
import json
from models.base_model import BaseModel

class FileStorage:
    '''The FileStorage class provides methods
    for managing and persisting objects in a file.'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects
        """
        return dict(type(self).__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (class_instance): instance of a certain class
                particularly BaseModel or descendants
        """
        key = "{}.{}".format(type(self).__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        
        for k, v in type(self).__objects.items():
            data[k] = v.to_dict()

        with open(type(self).__file_path, "w") as f:
            json.dump(data, f, indent = 2)

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
            otherwise, do nothing. If the file doesn’t exist,
            no exception should be raised)
        """
        try:
            with open(type(self).__file_path, "r") as f:
                dic = json.load(f)
                for k, v in dic.items():
                    type(self).__objects[k] = globals()[v["__class__"]](**v)
        except FileNotFoundError:
            pass
