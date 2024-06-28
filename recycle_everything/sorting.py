
from abc import ABC, abstractmethod

from recycle_everything import Dimensions
from recycle_everything.objects import Object
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
