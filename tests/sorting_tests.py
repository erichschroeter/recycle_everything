
import unittest
from recycle_everything import Dimensions
from recycle_everything.materials import Cardboard, Composition, Glue
from recycle_everything.objects import ObjectFactory

from recycle_everything.sorting import ABVolumeSorter
from recycle_everything.transportation import Conveyor


class TestVolumeSorter(unittest.TestCase):
    def setUp(self) -> None:
        self.objects = ObjectFactory(Dimensions(10, 10, 10), [Composition(Cardboard, 90), Composition(Glue, 10)])

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
