'''user module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''The class defines a User model with attributes for email, password, first name, and last name.'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method for a class, which calls the constructor of the
        parent class.
        """
        super().__init__(*args, **kwargs)
