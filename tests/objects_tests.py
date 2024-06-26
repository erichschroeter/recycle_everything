import unittest

from recycle_everything.objects import camel_case_to_lowercase_readable


class TestCamelCaseToLowercaseReadable(unittest.TestCase):

    def test_cardboard_box(self):
        self.assertEqual('cardboard box', camel_case_to_lowercase_readable('CardboardBox'))
