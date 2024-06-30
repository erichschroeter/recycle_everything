from abc import ABC
import typing


class Material(ABC):
    pass

class Cardboard(Material):
    pass

class Glue(Material):
    pass

class Conveyor:
    def __init__(self, output):
        self.output = output

    def __repr__(self):
        return f'Conveyor({self.output})'

# Create instances of Conveyor
conveyor_cardboard = Conveyor('cardboard output')
conveyor_glue = Conveyor('glue output')

# Create a dictionary mapping Material classes to Conveyor instances
output_conveyors = {Cardboard: conveyor_cardboard, Glue: conveyor_glue}

class Sorter:
    def __init__(self, mapping: typing.Dict[type[Material], Conveyor], other: Conveyor) -> None:
        self.mapping = mapping
        self.other = other

    def sort(self, object: Material) -> Conveyor:
        if object in self.mapping:
            return self.mapping[object]
        return self.other

# Check if a material exists in the dictionary
material = Cardboard
if material in output_conveyors:
    print(f'Redirecting {material} to {output_conveyors[material]}')

other_conveyor = Conveyor('other output')
sorter = Sorter(output_conveyors, other_conveyor)
obj = Cardboard()
conveyor = sorter.sort(obj)
print(f'Redirecting {obj} to {conveyor}')
