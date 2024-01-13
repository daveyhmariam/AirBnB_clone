'''base model for the model objects'''
import uuid
import datetime
import models


class BaseModel:
    '''The `BaseModel` class is a base class that provides common functionality for other classes, such as
    initializing attributes, saving changes, and converting attributes to a dictionary representation.'''
    
    def __init__(self, *args, **kwargs):
        """
        The function initializes an object and sets its attributes based on the provided keyword
        arguments.
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        The __str__ function returns a string representation of an object, including its class name, id,
        and attributes.
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        The function updates the "updated_at" attribute of an object and saves the changes to the
        storage.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        The function `to_dict` converts an object's attributes into a dictionary, including the object's
        class name and the ISO formatted creation and update timestamps.
        :return: The method `to_dict` returns a dictionary representation of the object.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
