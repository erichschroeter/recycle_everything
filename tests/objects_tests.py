import unittest

from recycle_everything.materials import Cardboard, Composition, CompositionError
from recycle_everything.objects import camel_case_to_lowercase_readable


class TestCamelCaseToLowercaseReadable(unittest.TestCase):

    def test_cardboard_box(self):
        self.assertEqual('cardboard box', camel_case_to_lowercase_readable('CardboardBox'))


class TestObject(unittest.TestCase):
    def test_composition_error_when_percentage_over_100(self):
        self.assertRaises(CompositionError, Cardboard, [Composition(Cardboard, 101)])
