from utils import FileReader, FileWriter, rand_int, rand_string


class Movie:
    RAND_NAME_LENGTH = 10
    RAND_YEAR_MIN = 1950
    RAND_YEAR_MAX = 2021

    def __init__(self) -> None:
        super().__init__()

        self.title = ""
        self.year = 0

    def input(self, file: FileReader):
        self.title = file.read_string()
        self.year = file.read_int()

    def input_random(self):
        self.title = rand_string(Movie.RAND_NAME_LENGTH)
        self.year = rand_int(Movie.RAND_YEAR_MIN, Movie.RAND_YEAR_MAX)

    def output(self, file: FileWriter):
        pass

    def quotient(self) -> float:
        return 1.0 * self.year / float(len(self.title))
