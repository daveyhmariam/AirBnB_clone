'''The `Place` class is a subclass of `BaseModel` and represents a place with various'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''# The `Place` class is a subclass of `BaseModel` and represents a place with various attributes such
    as city ID, user ID, name, description, number of rooms, number of bathrooms, maximum number of
    guests, price per night, latitude, longitude, and a list of amenity IDs.'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        The above function is the constructor method for a class, which calls the constructor of its
        parent class.
        """
        super().__init__(*args, **kwargs)
