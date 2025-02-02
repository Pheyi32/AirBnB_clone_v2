#!/usr/bin/python3
"""Tests for the Amenity Class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest


class test_Amenity(test_basemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipUnless(os.getenv("HBNB_TYPE_STORAGE") == "db",
                         "for db storage")
    def test_name2(self):
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str)
