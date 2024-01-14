'''The Review class is a subclass of the BaseModel
class and represents a review with attributes for
place_id, user_id, and text.'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''The Review class is a subclass of BaseModel
    and represents a review with attributes'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method
        for a class, which calls the constructor of the
        parent class.
        """
        super().__init__(*args, **kwargs)
