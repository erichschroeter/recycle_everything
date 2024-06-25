
import logging
import unittest

from recycle_everything import ONE_METER, Area, Dimensions
from recycle_everything.disassembly import AssemblyTooSmallError, Shredder
from recycle_everything.assembly import CardboardBox, AssemblyFactory
from recycle_everything.materials import Cardboard

ONE_CUBIC_METER = Dimensions(ONE_METER, ONE_METER, ONE_METER)

class TestShredder(unittest.TestCase):

    def setUp(self):
        self.item_factory = AssemblyFactory()

    def test_disassemble_cardboard_box_outputs_cardboard_particles(self):
        disassembler = Shredder(input_area=Area(ONE_METER, ONE_METER))
        items = disassembler.disassemble(self.item_factory.create_item('cardboard box', ONE_CUBIC_METER))
        self.assertEqual(items[0], Cardboard)


if __name__ == '__main__':
    disassembler = Shredder()
    item = AssemblyFactory().create_item('cardboard box', Dimensions(5, 10, 7))
    logging.warn(f'created: {item}')
    items = disassembler.disassemble(item)
    print(items)
    # unittest.main()

