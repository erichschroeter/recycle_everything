
from abc import ABC, abstractmethod
import inspect
import logging
import sys

from recycle_everything import Dimensions
from recycle_everything.materials import Cardboard, Material


class AssemblyFactory:
    def create_item(self, item_name: str, dimension: Dimensions):
        """
        Attempts to find the class closest to the given item_name within this module and returns an instance of it.
        """
        item_name = item_name.lower().replace(' ', '')
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if name.lower() == item_name.lower() and issubclass(obj, Assembly):
                logging.debug(f'Creating item: {name}')
                return obj(dimensions=dimension)
        logging.error(f'Assembly not supported: {item_name}')


class Assembly(ABC):
    def __init__(self, name: str, dimensions: Dimensions) -> None:
        super().__init__()
        self.name = name
        self.dimensions = dimensions

    @abstractmethod
    def materials(self) -> list[Material]:
        pass

class CardboardBox(Assembly):
    def __init__(self, dimensions: Dimensions) -> None:
        super().__init__('cardboard box', dimensions)

    def materials(self):
        return [Cardboard]

class Diaper(Assembly):
    pass

class CircuitBoard(Assembly):
    pass

if __name__ == '__main__':
    factory = AssemblyFactory()
    print(factory.create_item('cardboard box'))