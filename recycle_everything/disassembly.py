
from abc import ABC, abstractmethod
import logging

from recycle_everything.items import ItemFactory


class DisassemblyError(Exception):
    pass

class ItemTooSmallError(DisassemblyError):
    def __init__(self, item):
        super(DisassemblyError, self).__init__()
        self.item = item

    def __str__(self) -> str:
        return f'Item too small for disassembly: {self.item}'

class ItemTooLargeError(DisassemblyError):
    def __init__(self, item):
        super(DisassemblyError, self).__init__()
        self.item = item

    def __str__(self) -> str:
        return f'Item too large for disassembly: {self.item}'

class Disassembler(ABC):
    @abstractmethod
    def breakdown(self, item_name):
        pass

class SmallShredder(Disassembler):
    def breakdown(self, item_name):
        pass

class MediumShredder(Disassembler):
    def _within_size_range(self, cubic_millimeters):
        return cubic_millimeters > 10 and cubic_millimeters <= 100

    def breakdown(self, item_name):
        factory = ItemFactory()
        item = factory.create_item(item_name)
        # if item and self._within_size_range(item.cubic_millimeters()):
        if item:
            return item.breakdown_names()
        logging.warn(f'Failed to breakdown: {item_name}')

class LargeShredder(Disassembler):
    def minimum_cubic_millimeters(self):
        return 300*300*300

    def maximum_cubic_millimeters(self):
        return 300*600*600

    def breakdown(self, item_name):
        factory = ItemFactory()
        item = factory.create_item(item_name)
        if item:
            cmm = item.cubic_millimeters()
            if cmm < self.minimum_cubic_millimeters():
                raise ItemTooSmallError(item=item)
            if cmm > self.maximum_cubic_millimeters():
                raise ItemTooLargeError(item=item)
            return item.breakdown_names()
        logging.warn(f'Failed to breakdown: {item_name}')
