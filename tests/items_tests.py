
import unittest

from recycle_everything.items import BreadSlice, Sandwich


class TestBreadSlice(unittest.TestCase):

    def test_breaks_down_to_single_item(self):
        item = BreadSlice()
        pieces = item.breakdown_names()
        self.assertEqual(len(pieces), 1)


class TestSandwich(unittest.TestCase):

    def test_breaks_down_to_multiple_item(self):
        item = Sandwich()
        pieces = item.breakdown_names()
        self.assertEqual(len(pieces), 3)


if __name__ == '__main__':
    unittest.main()
