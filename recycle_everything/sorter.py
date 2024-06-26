
from abc import ABC, abstractmethod

from recycle_everything.objects import Object


class Sorter(ABC):
    def __init__(self, url: str = None) -> None:
        super().__init__()
        self.url = None

    """
    A Sorter identifies Objects and sorts them by material.
    """
    @abstractmethod
    def identify(self, object: Object):
        pass


class SorterFactory:
    def create(self, manufacturer_and_model: str) -> Sorter:
        if manufacturer_and_model == 'Bollegraaf RoBB-AQC':
            return Sorter(url='https://www.bollegraaf.com/en/products/rob-aqc-robot-sorting-system/')
        raise NotImplementedError(f'Sorter not supported: {manufacturer_and_model}')
