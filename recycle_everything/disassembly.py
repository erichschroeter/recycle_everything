
from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging

from recycle_everything import Area, BaseRecycleEverythingError, Dimensions
from recycle_everything.materials import Material
from recycle_everything.objects import Object


class DisassemblyError(BaseRecycleEverythingError):
    pass

class ObjectTooSmallError(DisassemblyError):
    def __init__(self, item):
        super(DisassemblyError, self).__init__()
        self.item = item

    def __str__(self) -> str:
        return f'Object too small for disassembly: {self.item}'

class ObjectTooLargeError(DisassemblyError):
    def __init__(self, input_area: Area, item: Object):
        super(DisassemblyError, self).__init__()
        self.input_area = input_area
        self.item = item

    def __str__(self) -> str:
        return f'Object {self.item.name()} ({self.item.dimensions}) too large for disassembly input {self.input_area}'


class Disassembler(ABC):
    @abstractmethod
    def disassemble(self, item_name):
        pass


@dataclass
class ParticleOutput:
    material: Material
    quantity: int

class Shredder(Disassembler):
    def __init__(self, input_area: Area, output_dimensions: Dimensions, url: str = None) -> None:
        super().__init__()
        self.input_area = input_area
        self.output_particle_dimensions = output_dimensions
        self.url = url

    def disassemble(self, item: Object):
        d = item.dimensions
        sorted_dimensions = sorted([d.width_mm, d.length_mm, d.height_mm])
        print(sorted_dimensions)
        # Assume as long as the item is smaller than the shredder's input dimensions, it can be shredded.
        if sorted_dimensions[0] > self.input_area.width_mm and sorted_dimensions[1] > self.input_area.width_mm:
            raise ObjectTooLargeError(input_area=self.input_area, item=item)
        # Figure out what % of new Objects to create for each material based on volume.
        output_particle_quanity = item.dimensions.volume() / self.output_particle_dimensions.volume()
        return [ParticleOutput(comp.material, output_particle_quanity*comp.percentage/100.0) for comp in item.composition]


class ShredderFactory:
    def create_shredder(self, manufacturer_and_model: str) -> Shredder:
        if manufacturer_and_model == 'Franklin Miller Taskmaster TM8512':
            return Shredder(input_area=Area(216, 305),
                            url='https://www.franklinmiller.com/product/taskmaster-tm8500-shredder')
        if manufacturer_and_model == 'Franklin Miller Taskmaster TM8516':
            return Shredder(input_area=Area(216, 406),
                            url='https://www.franklinmiller.com/product/taskmaster-tm8500-shredder')
        if manufacturer_and_model == 'Franklin Miller Taskmaster TM8520':
            return Shredder(input_area=Area(216, 508),
                            url='https://www.franklinmiller.com/product/taskmaster-tm8500-shredder')
        if manufacturer_and_model == 'Franklin Miller Taskmaster TM8524':
            return Shredder(input_area=Area(216, 610),
                            url='https://www.franklinmiller.com/product/taskmaster-tm8500-shredder')
        if manufacturer_and_model == 'Franklin Miller Taskmaster TM8532':
            return Shredder(input_area=Area(216, 813),
                            url='https://www.franklinmiller.com/product/taskmaster-tm8500-shredder')
        raise NotImplementedError(f'Shredder not supported: {manufacturer_and_model}')
