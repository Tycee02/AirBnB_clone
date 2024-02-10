#!/usr/bin/python3
"""
Contains the Test BaseModel class
"""

from datetime import datetime
import unittest
import models
BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel classs"""

    def test_uuid(self):
        """Test the uuid on instances"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertIsInstance(bm2, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)


if __name__ == '__main__':
    unittest.main()
