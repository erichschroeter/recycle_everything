
from abc import ABC, abstractmethod
from typing import Dict

from recycle_everything import Dimensions
from recycle_everything.materials import Cardboard, Composition, Glue, Material
from recycle_everything.objects import Object, ObjectFactory
from recycle_everything.transportation import Conveyor


class Sorter(ABC):
    def __init__(self, url: str = None) -> None:
        super().__init__()
        self.url = None

    """
    A Sorter identifies Objects and sorts them by material.
    """
    @abstractmethod
    def sort(self, object: Object) -> Conveyor:
        pass


class SorterFactory:
    def create(self, manufacturer_and_model: str) -> Sorter:
        if manufacturer_and_model == 'Bollegraaf RoBB-AQC':
            return Sorter(url='https://www.bollegraaf.com/en/products/rob-aqc-robot-sorting-system/')
        raise NotImplementedError(f'Sorter not supported: {manufacturer_and_model}')


class ABVolumeSorter(Sorter):
    def __init__(self, volume_greater_than_threshold: Dimensions, conveyor_a: Conveyor, conveyor_b: Conveyor, url: str = None) -> None:
        """
        Sorts based on volume. If the volume of an object surpasses the specified threshold,
        then the sorter will direct to conveyor B, else conveyor A.
        """
        super().__init__(url)
        self.volume_greater_than_threshold = volume_greater_than_threshold
        self.conveyor_a = conveyor_a
        self.conveyor_b = conveyor_b

    def sort(self, object: Object) -> Conveyor:
        if object.dimensions > self.volume_greater_than_threshold:
            return self.conveyor_b
        return self.conveyor_a


class MaterialSorter(Sorter):
    def __init__(self, materials_map: Dict[type[Material], Conveyor], reject_conveyor: Conveyor, url: str = None) -> None:
        """
        Sorts based on material. If the material is singular and within the specified materials_map,
        then the sorter will direct to the respective conveyor, else the reject conveyor.
        """
        super().__init__(url)
        self.materials_map = materials_map
        self.reject_conveyor = reject_conveyor

    def sort(self, object: Object) -> Conveyor:
        if len(object.composition) == 1:
            print(f'MATERIAL: {object.composition[0].material}')
            material = object.composition[0].material
            print(f'Checking for {material} IN {self.materials_map}')
            if material in self.materials_map:
                print(f'MaterialSorter: {self.materials_map[material]}')
                return self.materials_map[material]
        print(f'reject MaterialSorter: {self.reject_conveyor}')
        return self.reject_conveyor

if __name__ == '__main__':
    factory = ObjectFactory(materials=[Cardboard])
    p = factory.create('cardboard')
    conveyor_cardboard = Conveyor(label='cardboard conveyor')
    conveyor_glue = Conveyor(label='glue conveyor')
    sorter = MaterialSorter(materials_map={Cardboard: conveyor_cardboard, Glue: conveyor_glue}, reject_conveyor=Conveyor(label='reject conveyor'))
    print(sorter.sort(p))
