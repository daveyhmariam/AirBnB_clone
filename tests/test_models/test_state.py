#!/usr/bin/python3
'''The above class is a unit test class for the State model, testing its instance, subclass,
initialization, and attributes.'''
import unittest
import datetime
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    '''The Test_State class is a unit test class that tests the State class, checking if it is an instance
    of State, a subclass of BaseModel, and if its attributes have the correct types.'''

    @classmethod
    def setUpClass(cls):
        """
        The function sets up a class by creating an instance of the State class and assigning it to the
        class attribute "state1".
        """
        cls.state1 = State()

    def test_instance(self):
        """
        The function tests if an object is an instance of the State class.
        """
        self.assertIsInstance(self.state1, State)

    def test_sub_class(self):
        """
        The function tests if the class State is a subclass of the class BaseModel.
        """
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_init(self):
        """
        The function `test_init` checks the types of the attributes `id`, `created_at`, and `updated_at` of
        an object.
        """
        self.assertEqual(type(self.state1.id), str)
        self.assertEqual(type(self.state1.created_at), datetime.datetime)
        self.assertEqual(type(self.state1.updated_at), datetime.datetime)

    def test_attribute(self):
        """
        The function `test_attribute` checks if the `name` attribute of `self.state1` is of type `str`.
        """
        self.assertEqual(type(self.state1.name), str)

if __name__ == "__main__":
    unittest.loader()
