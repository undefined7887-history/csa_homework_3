from movie import Movie
from enum import Enum

from utils import FileReader, FileWriter, rand_int


class CartoonType(Enum):
    DRAW = "draw"
    PUPPET = "puppet"
    PLASTICINE = "plasticine"

    def from_string(value: str):
        for entry in CartoonType:
            if entry.value == value:
                return entry

        return CartoonType.DRAW

    def from_random():
        return [entry for entry in CartoonType][rand_int(0, 2)]


class Cartoon(Movie):
    def __init__(self) -> None:
        super().__init__()
        self.type = CartoonType.DRAW

    def input(self, file: FileReader):
        super().input(file)

        self.type = CartoonType.from_string(file.read_string())

    def input_random(self):
        super().input_random()

        self.type = CartoonType.from_random()

    def output(self, file: FileWriter):
        super().output(file)

        file.write_line(
            "Cartoon: name = %s, year = %s, type = %s" %
            (self.title,
             self.year,
             self.type.value)
        )
