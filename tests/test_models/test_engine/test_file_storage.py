#!/usr/bin/python3
'''The above class is a unit test for the FileStorage class, testing its methods such as all(), new(),
save(), and reload().'''
import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_FileStorage(unittest.TestCase):
    '''The `Test_FileStorage` class is a unit test class that tests the functionality of the `FileStorage`
    class.'''
    @classmethod
    def setUpClass(cls):
        """
        The setUpClass function initializes a FileStorage object and a BaseModel object as class
        attributes.
        """
        cls.storage1 = FileStorage()
        cls.model1 = BaseModel()
    
    def test_all(self):
        key = BaseModel.__name__ + "." + self.model1.id

        self.assertEqual(self.model1, self.storage1.all()[key])
        self.assertEqual(type(self.storage1.all()), dict)
    
    def test_new(self):
        key = BaseModel.__name__ + "." + self.model1.id

        self.assertEqual(self.model1, self.storage1.all()[key])
    
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
        data = {}
        for key, value in self.storage1.all().items():
            data[key] = value.to_dict()

        self.storage1.save()
        json_string = json.dumps(data, indent=2)
        file_string = self.file_read("file.json")

        self.assertEqual(json_string, file_string)

    def test_reload(self):
        model2 = BaseModel()
        key = BaseModel.__name__ + "." + model2.id
        
        self.storage1.reload()
        obj_rep = self.storage1.all()[key]
        self.assertEqual(model2.to_dict(),obj_rep.to_dict())

if __name__ == "__main__":
    unittest.loader()
