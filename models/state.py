'''state class module'''
from models.base_model import BaseModel


class State(BaseModel):
    '''The `State` class is a subclass of `BaseModel`
    and has a constructor method that calls the
    constructor of the parent class.'''
    name = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method
        for a class, which calls the constructor of the
        parent class.
        """
        super().__init__(*args, **kwargs)
