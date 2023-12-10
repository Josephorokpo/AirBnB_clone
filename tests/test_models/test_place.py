#!/usr/bin/env python3
"""
"""

import unittest
from models.place import Place
import models.place


class TestPlace(unittest.TestCase):
    def test_module_doc(self):
        self.assertIsNotNone(models.place.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_city_id(self):
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(isinstance(place.city_id, str))

    def test_attribute_user_id(self):
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(isinstance(place.user_id, str))

    def test_attribute_name(self):
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(isinstance(place.name, str))

    def test_attribute_description(self):
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(isinstance(place.description, str))

    def test_attribute_number_rooms(self):
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(isinstance(place.number_rooms, int))

    def test_attribute_number_bathrooms(self):
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(isinstance(place.number_bathrooms, int))

    def test_attribute_max_guest(self):
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(isinstance(place.max_guest, int))

    def test_attribute_price_by_night(self):
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(isinstance(place.price_by_night, int))

    def test_attribute_latitude(self):
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(isinstance(place.latitude, float))

    def test_attribute_longitude(self):
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(isinstance(place.longitude, float))

    def test_attribute_amenity_ids(self):
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        self.assertTrue(isinstance(place.amenity_ids, list))


if __name__ == "__main__":
    unittest.main()
