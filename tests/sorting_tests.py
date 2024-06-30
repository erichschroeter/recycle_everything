
import unittest
from recycle_everything import Dimensions
from recycle_everything.materials import Cardboard, Composition, Glue
from recycle_everything.objects import ObjectFactory

from recycle_everything.sorting import ABVolumeSorter, MaterialSorter
from recycle_everything.transportation import Conveyor


class TestMaterialSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.objects = ObjectFactory(materials=[Composition(Cardboard, 90), Composition(Glue, 10)], dimensions=Dimensions(10, 10, 10))

    def test_sort_cardboard(self):
        box = self.objects.create('cardboard')
        conveyor_cardboard = Conveyor(label='cardboard conveyor')
        conveyor_glue = Conveyor(label='glue conveyor')
        conveyor_other = Conveyor(label='other conveyor')
        sorter = MaterialSorter(materials_map={Cardboard: conveyor_cardboard, Glue: conveyor_glue}, reject_conveyor=conveyor_other)
        self.assertEqual(conveyor_cardboard, sorter.sort(box))

    # def test_sort_glue(self):
    #     box = self.objects.create('cardboard box')
    #     conveyor_cardboard = Conveyor()
    #     conveyor_glue = Conveyor()
    #     conveyor_other = Conveyor()
    #     sorter = MaterialSorter(materials_map={Cardboard: conveyor_cardboard, Glue: conveyor_glue}, reject_conveyor=conveyor_other)
    #     self.assertEqual(conveyor_cardboard, sorter.sort(box))

    # def test_sort_box(self):
    #     box = self.objects.create('cardboard box')
    #     conveyor_cardboard = Conveyor()
    #     conveyor_glue = Conveyor()
    #     conveyor_other = Conveyor()
    #     sorter = MaterialSorter(materials_map={Cardboard: conveyor_cardboard, Glue: conveyor_glue}, reject_conveyor=conveyor_other)
    #     self.assertEqual(conveyor_cardboard, sorter.sort(box))


class TestVolumeSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.objects = ObjectFactory(materials=[Composition(Cardboard, 90), Composition(Glue, 10)], dimensions=Dimensions(10, 10, 10))

    def test_sort_greater_than_threshold(self):
        box = self.objects.create('cardboard box', dimensions=Dimensions(11, 11, 11))
        conveyor_a = Conveyor()
        conveyor_b = Conveyor()
        sorter = ABVolumeSorter(volume_greater_than_threshold=Dimensions(10, 10, 10), conveyor_a=conveyor_a, conveyor_b=conveyor_b)
        self.assertEqual(conveyor_b, sorter.sort(box))

    def test_sort_less_than_threshold(self):
        box = self.objects.create('cardboard box', dimensions=Dimensions(9, 9, 9))
        conveyor_a = Conveyor()
        conveyor_b = Conveyor()
        sorter = ABVolumeSorter(volume_greater_than_threshold=Dimensions(10, 10, 10), conveyor_a=conveyor_a, conveyor_b=conveyor_b)
        self.assertEqual(conveyor_a, sorter.sort(box))

    def test_sort_equal_to_threshold(self):
        box = self.objects.create('cardboard box', dimensions=Dimensions(10, 10, 10))
        conveyor_a = Conveyor()
        conveyor_b = Conveyor()
        sorter = ABVolumeSorter(volume_greater_than_threshold=Dimensions(10, 10, 10), conveyor_a=conveyor_a, conveyor_b=conveyor_b)
        self.assertEqual(conveyor_a, sorter.sort(box))
