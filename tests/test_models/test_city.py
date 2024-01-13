#!/usr/bin/python3
'''The above class is a unit test class for the City class, testing its instance, subclass, and
initialization.'''
import unittest
import datetime
from models.city import City
from models.base_model import BaseModel


class Test_city(unittest.TestCase):
    '''# The Test_city class is a unit test class that tests the functionality and attributes of the City
        class.'''

    @classmethod
    def setUpClass(cls):
        """
        The above function is a class method that sets up a class variable called "city1" as an instance
        of the "City" class.
        """
        cls.city1 = City()

    def test_instance(self):
        """
        The function tests if an object is an instance of the City class.
        """
        self.assertIsInstance(self.city1, City)

    def test_sub_class(self):
        """
        The function tests if the class City is a subclass of the class BaseModel.
        """
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_init(self):
        """
        The function tests the initialization of a City object by checking the types of its attributes.
        """
        self.assertEqual(type(self.city1.state_id), str)
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.id), str)
        self.assertEqual(type(self.city1.created_at), datetime.datetime)
        self.assertEqual(type(self.city1.updated_at), datetime.datetime)

if __name__ == "__main__":
    unittest.loader()
