#!/usr/bin/python3
'''The TestBaseModel class is a unit test class for the BaseModel class, testing its initialization,
 string representation, saving to file, conversion to dictionary, and attribute types.'''
from models.base_model import BaseModel
import unittest
import datetime
import json
from models import storage 


class TestBaseModel(unittest.TestCase):
    '''The TestBaseModel class contains unit tests for the BaseModel class in Python.'''

    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function initializes a class variable called model1 with an instance of the
        BaseModel class.
        """
        cls.model1 = BaseModel()

    def test_instance(self):
        """
        The function tests if the instance of `self.model1` is of type `BaseModel`.
        """
        self.assertAlmostEqual(type(self.model1), BaseModel)

    def test_init_no_paramenter(self):
        """
        The function tests the initialization of an object and checks the types of its attributes.
        """
        self.assertEqual(type(self.model1.id), str)
        self.assertEqual(type(self.model1.created_at), datetime.datetime)
        self.assertEqual(type(self.model1.updated_at), datetime.datetime)
        self.assertEqual(storage.all()[BaseModel.__name__ + "." + self.model1.id], self.model1)

    def test_init_from_dict(self):
        """
        The function tests if a new instance of a BaseModel can be created from a dictionary
        representation.
        """
        class_rep = self.model1.to_dict()
        model2 = BaseModel(**class_rep)
        self.assertEqual(model2.id, self.model1.id)
        self.assertEqual(model2.created_at, self.model1.created_at)
        self.assertEqual(model2.updated_at, self.model1.updated_at)
    
    def test_str(self):
        """
        The function `test_str` tests the `__str__` method of a class by comparing the formatted string
        representation of an object with the expected string.
        """
        form = "[{}] ({}) {}".format(type(self.model1).__name__, self.model1.id, self.model1.__dict__)
        self.assertEqual(form, str(self.model1))

    def file_read(self, file_path):
        """
        The function reads the contents of a file and returns them as a string, or returns None if the
        file is not found.
        """
        try:
            with open(file_path, "r") as f:
                return f.read()
        except FileNotFoundError:
            pass

    def test_save(self):
        """
        The `test_save` function tests if the `updated_at` attribute of a model is updated after calling
        the `save` method, and then it reads data from a file and converts it to a JSON string.
        """
        up_date = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, up_date)

        data = {}
        for key, value in storage.all().items():
            data[key] = value.to_dict()

        json_string = json.dumps(data, indent=2)
        file_string = self.file_read("file.json")

        self.assertEqual(json_string, file_string)
    
    def test_to_dict(self):
        """
        The function `test_to_dict` creates a dictionary representation of an object and adds additional
        key-value pairs for class name, creation time, and update time.
        """
        dic_rep = self.model1.to_dict().copy()
        dic_rep["__class__"] = "BaseModel"
        dic_rep["created_at"] = self.model1.created_at.isoformat()
        dic_rep["updated_at"] = self.model1.updated_at.isoformat()

        self.assertDictEqual(dic_rep, self.model1.to_dict())

    def test_type_of_attribute(self):
        """
        The function tests the type of attributes in a model object.
        """
        self.assertEqual(type(self.model1.id), str)
        self.assertEqual(type(self.model1.created_at), datetime.datetime)
        self.assertEqual(type(self.model1.updated_at), datetime.datetime)

    def test_to_dict_date_type(self):
        """
        The function tests that the "created_at" and "updated_at" keys in the dictionary returned by the
        "to_dict" method are of type string.
        """
        self.assertEqual(type(self.model1.to_dict()["created_at"]), str)
        self.assertEqual(type(self.model1.to_dict()["updated_at"]), str)
    
    def is_iso_format(self, str_rep_of_date):
        """
        The function checks if a given string representation of a date is in ISO format.
        """
        try:
            datetime.datetime.strptime(str_rep_of_date, "%Y-%m-%dT%H:%M:%S.%f")
            return True
        except ValueError:
            return False

    def test_check_iso_format(self):
        """
        The function `test_check_iso_format` checks if the `created_at` and `updated_at` attributes of
        `model1` are in ISO format.
        """
        self.assertEqual(self.is_iso_format(self.model1.to_dict()["created_at"]), True)
        self.assertEqual(self.is_iso_format(self.model1.to_dict()["updated_at"]), True)

if __name__ == "__main__":
    unittest.loader()
