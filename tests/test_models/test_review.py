#!/usr/bin/python3
'''The Test_Review class contains unit tests for
the Review class, checking its instance, subclass,
initialization, and attributes.'''
import unittest
import datetime
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    '''The Test_Review class contains unit tests for
    the Review class, checking its instance, subclass,
    initialization, and attributes.'''

    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function initializes an instance
        of the Review class and assigns it to the
        review1 attribute of the class.
        """
        cls.review1 = Review()

    def test_instance(self):
        """
        The function `test_instance` checks if `self.review1`
        is an instance of the `Review` class.
        """
        self.assertIsInstance(self.review1, Review)

    def test_sub_class(self):
        """
        The function tests if the class Review is a subclass
        of BaseModel.
        """
        self.assertEqual(issubclass(Review, BaseModel), True)

    def test_init(self):
        """
        The function `test_init` checks the types of attributes
        `id`, `created_at`, and `updated_at` of an
        object `review1`.
        """
        self.assertEqual(type(self.review1.id), str)
        self.assertEqual(type(self.review1.created_at), datetime.datetime)
        self.assertEqual(type(self.review1.updated_at), datetime.datetime)

    def test_attribute(self):
        """
        The function tests the attribute types of the review1 object.
        """
        self.assertEqual(type(self.review1.place_id), str)
        self.assertEqual(type(self.review1.user_id), str)
        self.assertEqual(type(self.review1.text), str)


if __name__ == "__main__":
    unittest.loader()
