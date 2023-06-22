#!/usr/bin/python3
"""Tests for the Review Class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os
import unittest


@unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") != "db", "for db storage")
class test_review(test_basemodel):
    """ review test class"""

    def __init__(self, *args, **kwargs):
        """ review class init"""
        super().__init__(*args, **kwargs)
        self.value = Review

    def test_place_id(self):
        """ testing review place_id attr"""
        new = self.value(place_id="t567hgr4")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ testing review user_id attr"""
        new = self.value(user_id="232-456-789")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ testing review text attr"""
        new = self.value(text="")
        self.assertEqual(type(new.text), str)
