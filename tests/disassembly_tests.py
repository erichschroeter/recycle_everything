
import logging
import unittest

from recycle_everything.disassembly import ItemTooSmallError, LargeShredder, MediumShredder
from recycle_everything.items import BreadSlice, Sandwich


class TestMediumShredder(unittest.TestCase):

    def test_sandwich_breakdown(self):
        disassembler = MediumShredder()
        items = disassembler.breakdown('sandwich')
        self.assertEqual(3, len(items))


class TestLargeShredder(unittest.TestCase):

    def test_sandwich_too_small_to_breakdown(self):
        disassembler = LargeShredder()
        self.assertRaises(ItemTooSmallError, disassembler.breakdown, 'sandwich')


if __name__ == '__main__':
    logger = logging.getLogger()
    # logger.setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    # ch = logging.StreamHandler()
    # ch.setLevel(logging.DEBUG)
    # logger.addHandler(ch)
    disassembler = MediumShredder()
    items = disassembler.breakdown('sandwich')
    print(items)
    # unittest.main()

