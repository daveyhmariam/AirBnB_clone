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
    '''The FileStorage class provides methods
    for managing and persisting objects in a file.'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        The function returns all objects of the same
        type as the calling object.
        """
        return type(self).__objects

    def new(self, obj):
        """
        The function "new" adds an object to a dictionary
        with a key generated from the object's type
        name and id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        The `save` function saves the objects of a class
        to a file in JSON format.
        """
        data = {}

        for key, value in type(self).__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(data, f, indent=2)

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
        except FileNotFoundError:
            pass
