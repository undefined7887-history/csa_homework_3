from movie import Movie
from utils import FileReader, FileWriter, rand_int


class Fiction(Movie):
    RAND_DIRECTOR_NAME = 10

    def __init__(self) -> None:
        super().__init__()

        self.director = ""

    def input(self, file: FileReader):
        super().input(file)

        self.director = file.read_string()

    def input_random(self):
        super().input_random()

        self.director = rand_int(
            Fiction.RAND_DIRECTOR_NAME,
            Fiction.RAND_DIRECTOR_NAME,
        )

    def output(self, file: FileWriter):
        super().output(file)

        file.write_line(
            "Fiction: name = %s, year = %s, director = %s" %
            (self.title,
             self.year,
             self.director)
        )
