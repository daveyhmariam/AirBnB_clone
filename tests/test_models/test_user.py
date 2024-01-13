#!/usr/bin/python3
'''The above class is a unit test for the User
class, testing its instance, subclass, initialization,
and attributes.'''
import unittest
import datetime
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    '''The Test_User class is a unit test class
    that tests the attributes and methods of the User class.'''

    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function creates an instance
        of the User class and assigns it to the user1 variable.
        """
        cls.user1 = User()

    def test_instance(self):
        """
        The function `test_instance` checks if `self.user1`
        is an instance of the `User` class.
        """
        self.assertIsInstance(self.user1, User)

    def test_sub_class(self):
        """
        The function tests if the class User is a subclass
        of the class BaseModel.
        """
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_init(self):
        """
        The test_init function checks the types of attributes
        in the user1 object.
        """
        self.assertEqual(type(self.user1.id), str)
        self.assertEqual(type(self.user1.created_at), datetime.datetime)
        self.assertEqual(type(self.user1.updated_at), datetime.datetime)

    def test_attribute(self):
        """
        The function `test_attribute` checks the types of
        attributes of an object.
        """
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)


if __name__ == "__main__":
    unittest.loader()
