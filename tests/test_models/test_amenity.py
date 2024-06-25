#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up test methods."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down test methods."""
        del self.amenity

    def test_amenity_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test Amenity class attributes."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs."""
        a_dict = self.amenity.to_dict()
        self.assertEqual(type(a_dict), dict)
        for attr in self.amenity.__dict__:
            self.assertTrue(attr in a_dict)
            self.assertTrue("__class__" in a_dict)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        a_dict = self.amenity.to_dict()
        self.assertEqual(a_dict["__class__"], "Amenity")
        self.assertEqual(type(a_dict["created_at"]), str)
        self.assertEqual(type(a_dict["updated_at"]), str)
        self.assertEqual(a_dict["created_at"],
                         self.amenity.created_at.strftime(t_format))
        self.assertEqual(a_dict["updated_at"],
                         self.amenity.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output."""
        string = ("[Amenity] ({}) {}"
                  .format(self.amenity.id, self.amenity.__dict__))
        self.assertEqual(string, str(self.amenity))


if __name__ == "__main__":
    unittest.main()
