
import unittest
from recycle_everything import Area, Dimensions, InvalidValue, InvalidValue


class TestArea(unittest.TestCase):
    def test_negative_width_not_allowed(self):
        self.assertRaises(InvalidValue, Area, -1, 2)

    def test_negative_length_not_allowed(self):
        self.assertRaises(InvalidValue, Area, 2, -1)


class TestDimensions(unittest.TestCase):
    def test_negative_width_not_allowed(self):
        self.assertRaises(InvalidValue, Dimensions, -1, 2, 3)

    def test_negative_length_not_allowed(self):
        self.assertRaises(InvalidValue, Dimensions, 2, -1, 3)

    def test_negative_height_not_allowed(self):
        self.assertRaises(InvalidValue, Dimensions, 2, 3, -1)
