
from abc import ABC, abstractmethod


class Material(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

class OrganicMaterial(Material):
    def name(self):
        return 'organic material'

class Cardboard(Material):
    def name(self):
        return 'cardboard'

class Wood(Material):
    def name(self):
        return 'wood'

class Glass(Material):
    def name(self):
        return 'glass'

class Plastic(Material):
    def name(self):
        return 'plastic'

class Metal(Material):
    def name(self):
        return 'metal'
