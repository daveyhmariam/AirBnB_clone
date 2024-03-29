'''user module'''
from models.base_model import BaseModel

class User(BaseModel):
    """class User that inherits from BaseModel

    Args:
        BaseModel (Class):
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *arg, **kwargs):
        """Constructor method of the sub class user
        """
        super().__init__(*arg, **kwargs)
