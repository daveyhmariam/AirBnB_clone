#!/usr/bin/python3
"""defines all common attributes/methods for other classes:

"""
from datetime import datetime
import models
import uuid


class BaseModel():
    """Base class for models
    """
    name = "dave"
    def __init__(self, *args, **kwargs):
        """ Initializes object creation
            set instance attributes from kwargs if kwargs is not None
            otherwise creat attributes
        args:
            args (list, tuple): an iterable of positional args
            kwargs (ditionary): a dictionary of keyword args

        """
        if kwargs != {}:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        date_obj = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, k, date_obj)
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
    
    def __str__(self):
        """the string representation of objects
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """Public instance method to register the update time
        """
        self.updated_at = datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        Return: dictionary
        """
        instance_dictionary = self.__dict__.copy()
        class_name = self.__class__.__name__
        instance_dictionary.update({"__class__": class_name})
        instance_dictionary["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        instance_dictionary["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return instance_dictionary
