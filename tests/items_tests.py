
import unittest

from recycle_everything.assembly import CardboardBox, Dimensions


class TestCardboardBox(unittest.TestCase):

    def test_disassemble_materials(self):
        item = CardboardBox(Dimensions(100, 100, 100))
        self.assertEqual(len(item.materials()), 1)


if __name__ == '__main__':
    unittest.main()
