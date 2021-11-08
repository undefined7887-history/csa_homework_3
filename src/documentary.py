from movie import Movie
from utils import FileReader, FileWriter, rand_int


class Documentary(Movie):
    RAND_DURATION_MIN = 1000
    RAND_DURATION_MAX = 5000

    def __init__(self) -> None:
        super().__init__()

        self.duration = 0

    def input(self, file: FileReader):
        super().input(file)

        self.duration = file.read_int()

    def input_random(self):
        super().input_random()

        self.duration = rand_int(
            Documentary.RAND_DURATION_MIN,
            Documentary.RAND_DURATION_MAX
        )

    def output(self, file: FileWriter):
        super().output(file)

        file.write_line(
            "Documentary: name = %s, year = %s, duration = %d" %
            (self.title,
             self.year,
             self.duration)
        )
