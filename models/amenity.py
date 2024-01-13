#!/usr/bin/python3
'''The `Amenity` class is a subclass of `BaseModel` and has a `name` attribute.'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''The class `Amenity` is a subclass of `BaseModel` and has a `name` attribute.'''
    name = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method for a class, which calls the constructor of the
        parent class.
        """
        super().__init__(*args, **kwargs)
