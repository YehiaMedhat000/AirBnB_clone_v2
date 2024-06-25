#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up test methods."""
        self.review = Review()

    def tearDown(self):
        """Tear down test methods."""
        del self.review

    def test_review_inheritance(self):
        """Test that Review inherits from BaseModel."""
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        """Test Review class attributes."""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs."""
        r_dict = self.review.to_dict()
        self.assertEqual(type(r_dict), dict)
        for attr in self.review.__dict__:
            self.assertTrue(attr in r_dict)
            self.assertTrue("__class__" in r_dict)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct."""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r_dict = self.review.to_dict()
        self.assertEqual(r_dict["__class__"], "Review")
        self.assertEqual(type(r_dict["created_at"]), str)
        self.assertEqual(type(r_dict["updated_at"]), str)
        self.assertEqual(r_dict["created_at"],
                         self.review.created_at.strftime(t_format))
        self.assertEqual(r_dict["updated_at"],
                         self.review.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output."""
        string = ("[Review] ({}) {}"
                  .format(self.review.id, self.review.__dict__))
        self.assertEqual(string, str(self.review))


if __name__ == "__main__":
    unittest.main()
