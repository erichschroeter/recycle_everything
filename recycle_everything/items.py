
from abc import ABC, abstractmethod
import inspect
import logging
import sys


class BreakdownTree:
    """
    The idea for this is for every Item to have its own unique breakdown into smaller Items.
    """
    pass

class ItemFactory:
    def create_item(self, item_name: str):
        """
        Attempts to find the class closest to the given item_name within this module and returns an instance of it.
        """
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if name.lower() == item_name.lower() and issubclass(obj, Item):
                logging.debug(f'Creating item: {name}')
                return obj()
        logging.warn(f'Failed to create item: {item_name}')

class Material(ABC):
    @abstractmethod
    def name(self):
        pass

class Item(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def breakdown_names(self):
        pass

    @abstractmethod
    def cubic_millimeters(self) -> int:
        pass

class OrganicMaterial(Material):
    def name(self):
        return 'organic material'

class BreadSlice(Item):
    def name(self):
        return 'bread slice'

    def breakdown_names(self):
        return [OrganicMaterial().name()]

    def cubic_millimeters(self) -> int:
        return 10*50*50

class Meat(Item):
    def name(self):
        return 'meat'

    def breakdown_names(self):
        return [OrganicMaterial().name()]

    def cubic_millimeters(self) -> int:
        return 5*50*50

class Vegetable(Item):
    def name(self):
        return 'vegetable'

    def breakdown_names(self):
        return [OrganicMaterial().name()]

    def cubic_millimeters(self) -> int:
        return 7*50*50

class Sandwich(Item):
    def name(self):
        return 'sandwich'

    def breakdown_names(self):
        return [Meat().name(), Vegetable().name(), BreadSlice().name()]

    def cubic_millimeters(self) -> int:
        return BreadSlice().cubic_millimeters()*2 + Meat().cubic_millimeters() + Vegetable().cubic_millimeters()

class Diaper(Item):
    pass

class Wood(Item):
    pass

class GlassJar(Item):
    pass

class PlasticBottle(Item):
    pass

class AluminumCan(Item):
    pass

class CircuitBoard(Item):
    pass

if __name__ == '__main__':
    factory = ItemFactory()
    print(factory.create_item('sandwich'))