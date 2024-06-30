
from abc import ABC
from dataclasses import dataclass

from recycle_everything import BaseRecycleEverythingError


class Material(ABC):
    pass


class CompositionError(BaseRecycleEverythingError):
    pass

@dataclass
class Composition:
   material: type[Material]
   percentage: float


class Cardboard(Material):
    pass

class Glass(Material):
    pass

class Glue(Material):
    pass

class Metal(Material):
    pass

class OrganicMaterial(Material):
    pass

class Paper(Material):
    pass

class Plastic(Material):
    pass

class Rubber(Material):
    pass

class Wood(Material):
    pass
