
from abc import ABC
import inspect
import re
import sys

from recycle_everything import Dimensions
import recycle_everything
from recycle_everything.materials import Cardboard, Composition, Glue, Material

CAMEL_CASE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

def camel_case_to_lowercase_readable(name):
    return CAMEL_CASE_PATTERN.sub('_', name).lower().replace('_', ' ')


class ObjectFactory:
    def __init__(self, materials: list[Composition], dimensions: Dimensions = Dimensions(1, 1, 1)) -> None:
        self.materials = materials
        self.default_dimensions = dimensions

    def create(self, object_name: str, dimensions: Dimensions = None):
        """
        Attempts to find the class closest to the given object_name within this module and returns an instance of it.
        """
        object_name = object_name.lower()
        # Attempt to search through defined Object derivatives and convert class name from CamelCase to lowercase with spaces
        for class_name, obj in inspect.getmembers(sys.modules[__name__]):
            if camel_case_to_lowercase_readable(class_name) == object_name and issubclass(obj, Object):
                return obj(dimensions=dimensions if dimensions else self.default_dimensions, composition=self.materials)
        for class_name, material in inspect.getmembers(sys.modules['recycle_everything.materials']):
            if camel_case_to_lowercase_readable(class_name) == object_name and issubclass(material, Material):
                return Particle(material=self.materials, dimensions=dimensions if dimensions else self.default_dimensions)
        raise NotImplementedError(f'Object not supported: {object_name}')


class Object(ABC):
    def __init__(self, name: str, dimensions: Dimensions, composition: list[Composition]) -> None:
        super().__init__()
        self.name = name
        self.dimensions = dimensions
        self.composition = composition


class Particle(Object):
    def __init__(self, material: Material, dimensions: Dimensions = Dimensions(1, 1, 1)) -> None:
        super().__init__(str(material), dimensions, [Composition(material, 100)])


class CardboardBox(Object):
    def __init__(self, dimensions: Dimensions, composition: list[Composition]) -> None:
        super().__init__(name='cardboard box',
                         dimensions=dimensions,
                         composition=composition)

class Diaper(Object):
    pass

class CircuitBoard(Object):
    pass

if __name__ == '__main__':
    factory = ObjectFactory(materials=[Cardboard])
    print(factory.create('cardboard'))