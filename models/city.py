'''The City class is a subclass of BaseModel and
represents a city with a state ID and name.'''
from models.base_model import BaseModel


class City(BaseModel):
    '''The City class is a subclass of BaseModel
    and represents a city with a state ID and name.'''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method
        for a class, which calls the constructor of its
        parent class.
        """
        super().__init__(*args, **kwargs)
