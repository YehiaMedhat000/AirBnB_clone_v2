#!/usr/bin/python3
"""Unittest module for the State Class."""
import unittest
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test cases for the State class."""

    def setUp(self):
        """Set up test methods."""
        self.state = State()

    def tearDown(self):
        """Tear down test methods."""
        del self.state

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_state_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """Test State class attributes."""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs."""
        s_dict = self.state.to_dict()
        self.assertEqual(type(s_dict), dict)
        for attr in self.state.__dict__:
            self.assertTrue(attr in s_dict)
            self.assertTrue("__class__" in s_dict)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        s_dict = self.state.to_dict()
        self.assertEqual(s_dict["__class__"], "State")
        self.assertEqual(type(s_dict["created_at"]), str)
        self.assertEqual(type(s_dict["updated_at"]), str)
        self.assertEqual(s_dict["created_at"],
                         self.state.created_at.strftime(t_format))
        self.assertEqual(s_dict["updated_at"],
                         self.state.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output."""
        string = ("[State] ({}) {}"
                  .format(self.state.id, self.state.__dict__))
        self.assertEqual(string, str(self.state))

    # Additional test cases
    def test_name3(self):
        """Already existing test. Kept as is."""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == "__main__":
    unittest.main()
