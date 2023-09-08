import unittest
from unittest import TestCase
from POI import *

class TestPOI(TestCase):
    def setUp(self):
        self.poi = POI()

    def test_login_admin(self):
        self.assertEqual(self.poi.login("admin", "admin"), "admin")

    def test_login_user(self):
        self.assertEqual(self.poi.login("user01", "password"), "user")

    def test_login_fail(self):
        self.assertIsNone(self.poi.login("me", "me"))

    def test_get_poi_existing(self):
        self.assertEqual(self.poi.get_poi(1), "테스트용")

    def test_get_poi_non_existing(self):
        self.assertIsNone(self.poi.get_poi(2))

    def test_add_poi_with_name(self):
        self.assertEqual(self.poi.add_poi("마라탕집"), 2)

    def test_add_poi_without_name(self):
        self.assertIsNone(self.poi.add_poi(None))

    def test_edit_poi_valid(self):
        self.assertTrue(self.poi.edit_poi(1, "POI 수정"))

    def test_edit_poi_invalid(self):
        self.assertFalse(self.poi.edit_poi(2, "POI 수정"))

    def test_delete_poi_valid(self):
        self.assertTrue(self.poi.delete_poi(1))

    def test_delete_poi_invalid(self):
        self.assertFalse(self.poi.delete_poi(2))

if __name__ == "__main__":
    unittest.main()

