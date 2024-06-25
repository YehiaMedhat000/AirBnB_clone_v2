#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test cases for the User class."""

    def __init__(self, *args, **kwargs):
        """ Init the values """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test the first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test the last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Test the email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test the password """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def setUp(self):
        """Set up test methods."""
        self.user = User()

    def tearDown(self):
        """Tear down test methods."""
        del self.user

    def test_user_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Test User class attributes."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs."""
        u_dict = self.user.to_dict()
        self.assertEqual(type(u_dict), dict)
        for attr in self.user.__dict__:
            self.assertTrue(attr in u_dict)
            self.assertTrue("__class__" in u_dict)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u_dict = self.user.to_dict()
        self.assertEqual(u_dict["__class__"], "User")
        self.assertEqual(type(u_dict["created_at"]), str)
        self.assertEqual(type(u_dict["updated_at"]), str)
        self.assertEqual(u_dict["created_at"],
                         self.user.created_at.strftime(t_format))
        self.assertEqual(u_dict["updated_at"],
                         self.user.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output."""
        string = ("[User] ({}) {}"
                  .format(self.user.id, self.user.__dict__))
        self.assertEqual(string, str(self.user))

    # Existing test cases (kept as is)
    def test_first_name(self):
        """Test first_name attribute."""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test last_name attribute."""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test email attribute."""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test password attribute."""
        new = self.value()
        self.assertEqual(type(new.password), str)


if __name__ == "__main__":
    unittest.main()
