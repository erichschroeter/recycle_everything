
from abc import ABC, abstractmethod
import logging

from recycle_everything import Area
from recycle_everything.items import Assembly


class DisassemblyError(Exception):
    pass

class AssemblyTooSmallError(DisassemblyError):
    def __init__(self, item):
        super(DisassemblyError, self).__init__()
        self.item = item

    def __str__(self) -> str:
        return f'Assembly too small for disassembly: {self.item}'

class AssemblyTooLargeError(DisassemblyError):
    def __init__(self, input_area: Area, item: Assembly):
        super(DisassemblyError, self).__init__()
        self.input_area = input_area
        self.item = item

    def __str__(self) -> str:
        return f'Assembly {self.item.name()} ({self.item.dimensions}) too large for disassembly input {self.input_area}'

class Disassembler(ABC):
    @abstractmethod
    def disassemble(self, item_name):
        pass

class Shredder(Disassembler):
    def __init__(self, input_area: Area) -> None:
        super().__init__()
        self.input_area = input_area

    def disassemble(self, item: Assembly):
        d = item.dimensions
        sorted_dimensions = sorted([d.width_mm, d.length_mm, d.height_mm])
        print(sorted_dimensions)
        # Assume as long as the item is smaller than the shredder's input dimensions, it can be shredded.
        if sorted_dimensions[0] > self.input_area.width_mm and sorted_dimensions[1] > self.input_area.width_mm:
            raise AssemblyTooLargeError(input_area=self.input_area, item=item)
        return item.materials()
