'''base model for the model objects'''
import uuid
import datetime
import models


class BaseModel:
    '''The `BaseModel` class is a base class that
    provides common functionality for other classes, such as
    initializing attributes, saving changes, and
    converting attributes to a dictionary representation.'''

    def __init__(self, *args, **kwargs):
        """
        The function initializes an object and sets
        its attributes based on the provided keyword
        arguments.
        """
        if kwargs != {}:
            del kwargs["__class__"]
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """update the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dic = self.__dict__.copy()
        dic["__class__"] = str(type(self).__name__)
        dic["created_at"] = self.__dict__["created_at"].isoformat()
        dic["updated_at"] = self.__dict__["updated_at"].isoformat()
        return dic

    def __str__(self):
        """Human readable String representation of instance
        Return:
            str:
        """
        return f"[{str(type(self).__name__)}] ({self.id}) {self.__dict__}"
