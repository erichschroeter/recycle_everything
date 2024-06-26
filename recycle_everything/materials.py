
from abc import ABC
from dataclasses import dataclass


class Material(ABC):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name


@dataclass
class Composition:
   material: Material
   percentage: float


class Cardboard(Material):
    def __init__(self, name: str) -> None:
        super().__init__('cardboard')

class Glass(Material):
    def __init__(self, name: str) -> None:
        super().__init__('glass')

class Glue(Material):
    def __init__(self, name: str) -> None:
        super().__init__('glue')

class Metal(Material):
    def __init__(self, name: str) -> None:
        super().__init__('metal')

class OrganicMaterial(Material):
    def __init__(self, name: str) -> None:
        super().__init__('organic material')

class Paper(Material):
    def __init__(self, name: str) -> None:
        super().__init__('paper')

class Plastic(Material):
    def __init__(self, name: str) -> None:
        super().__init__('plastic')

class Rubber(Material):
    def __init__(self, name: str) -> None:
        super().__init__('rubber')

class Wood(Material):
    def __init__(self, name: str) -> None:
        super().__init__('wood')
