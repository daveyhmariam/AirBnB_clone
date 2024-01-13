'''class that handles object storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return type(self).__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}

        for key, value in type(self).__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(data, f, indent=2)

    def reload(self):
        try:
            with open(type(self).__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    type(self).__objects[key] = globals()[
                        value["__class__"]](**value)
        except FileNotFoundError:
            pass
