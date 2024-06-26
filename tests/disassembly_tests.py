
import logging
import unittest

from recycle_everything import ONE_CENTIMETER, ONE_CUBIC_METER, ONE_METER, Area, Dimensions, _init_logger
from recycle_everything.disassembly import Shredder
from recycle_everything.objects import ObjectFactory
from recycle_everything.materials import Cardboard, Composition, Glue


class TestShredder(unittest.TestCase):

    def setUp(self):
        self.item_factory = ObjectFactory()

    def test_disassemble_90_10_cardboard_box(self):
        disassembler = Shredder(input_area=Area(ONE_METER, ONE_METER),
                                output_dimensions=Dimensions(ONE_CENTIMETER, ONE_CENTIMETER, ONE_CENTIMETER))
        box = self.item_factory.create('cardboard box', ONE_CUBIC_METER, [Composition(Cardboard, 90.0), Composition(Glue, 10.0)])
        output = sorted(disassembler.disassemble(box), key=lambda x: x.material.__qualname__)  # sort alphabetically
        self.assertEqual(output[0].quantity, 900)  # 900 pieces of Cardboard
        self.assertEqual(output[1].quantity, 100)  # 100 pieces of Glue (tape)


if __name__ == '__main__':
    _init_logger(logging.INFO)
    disassembler = Shredder(input_area=Area(ONE_METER, ONE_METER),
                            output_dimensions=Dimensions(ONE_CENTIMETER, ONE_CENTIMETER, ONE_CENTIMETER))
    box = ObjectFactory().create('cardboard box',
                                 ONE_CUBIC_METER,
                                 [Composition(Cardboard, 90.0), Composition(Glue, 10.0)])
    logging.warn(f'created: {box}')
    items = disassembler.disassemble(box)
    print(items)
    # unittest.main()

