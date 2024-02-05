#!/usr/bin/python3
"""
Contains the Test BaseModel class
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel


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


if __name__ == '__main__':
    unittest.main()
