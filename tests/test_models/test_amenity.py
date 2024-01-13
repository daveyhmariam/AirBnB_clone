#!/usr/bin/python3
'''The above class is a unit test class for the Amenity class, testing its instance, subclass, and
initialization.'''
import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_amenity(unittest.TestCase):
    '''The Test_amenity class is a unit test class that tests the functionality and properties of the
        Amenity class.'''

    @classmethod
    def setUpClass(cls):
        """
        The above function is a class method that sets up a class variable called amenity1 as an
        instance of the Amenity class.
        """
        cls.amenity1 = Amenity()

    def test_instance(self):
        """
        The function tests if an object is an instance of a specific class.
        """
        self.assertIsInstance(self.amenity1, Amenity)

    def test_sub_class(self):
        """
        The function tests if the class Amenity is a subclass of the class BaseModel.
        """
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_init(self):
        """
        The function tests the initialization of an object by checking the types of its attributes.
        """
        self.assertEqual(type(self.amenity1.name), str)
        self.assertEqual(type(self.amenity1.id), str)
        self.assertEqual(type(self.amenity1.created_at), datetime.datetime)
        self.assertEqual(type(self.amenity1.updated_at), datetime.datetime)

if __name__ == "__main__":
    unittest.loader()
