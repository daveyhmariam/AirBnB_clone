#!/usr/bin/python3
'''The above class is a unit test for the Place class, checking its instance, subclass, initialization,
and attribute types.'''
import unittest
import datetime
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    '''The Test_Place class contains unit tests for the Place class, checking its instance, subclass,
    initialization, and attribute types.'''

    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function sets up a class by creating an instance of the Place class.
        """
        cls.place1 = Place()

    def test_instance(self):
        """
        The function tests if an instance is of a specific class.
        """
        self.assertIsInstance(self.place1, Place)

    def test_sub_class(self):
        """
        The function tests if the class "Place" is a subclass of "BaseModel".
        """
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_init(self):
        """
        The function tests the initialization of attributes in a class instance.
        """
        self.assertEqual(type(self.place1.id), str)
        self.assertEqual(type(self.place1.created_at), datetime.datetime)
        self.assertEqual(type(self.place1.updated_at), datetime.datetime)

    def test_attribute(self):
        """
        The function `test_attribute` checks the types of attributes of an object `place1` and asserts that
        they are of the expected types.
        """
        self.assertEqual(type(self.place1.city_id), str)
        self.assertEqual(type(self.place1.user_id), str)
        self.assertEqual(type(self.place1.name), str)
        self.assertEqual(type(self.place1.description), str)
        self.assertEqual(type(self.place1.number_rooms), int)
        self.assertEqual(type(self.place1.number_bathrooms), int)
        self.assertEqual(type(self.place1.max_guest), int)
        self.assertEqual(type(self.place1.price_by_night), int)
        self.assertEqual(type(self.place1.latitude), float)
        self.assertEqual(type(self.place1.longitude), float)
        self.assertEqual(type(self.place1.amenity_ids), list)

if __name__ == "__main__":
    unittest.loader()
