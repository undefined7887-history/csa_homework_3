from cartoon import Cartoon
from documentary import Documentary
from fiction import Fiction
from utils import FileReader, FileWriter, rand_int


class Container:
    def __init__(self) -> None:
        self.content = []

    def input(self, file: FileReader):
        while file.has_next():
            movie_type = file.read_int()
            movie_data = None

            if movie_type == 1:
                movie_data = Fiction()
            elif movie_type == 2:
                movie_data = Cartoon()
            elif movie_type == 3:
                movie_data = Documentary()

            movie_data.input(file)
            self.content.append(movie_data)

    def input_random(self, count: int):
        for _ in range(count):
            movie_type = rand_int(1, 3)

            if movie_type == 1:
                movie_data = Fiction()
            elif movie_type == 2:
                movie_data = Cartoon()
            elif movie_type == 3:
                movie_data = Documentary()

            movie_data.input_random()
            self.content.append(movie_data)

    def output(self, writer: FileWriter):
        writer.write_line("Container contains %d elements" % len(self.content))

        for i in range(len(self.content)):
            writer.write("%d) " % (i+1))

            self.content[i].output(writer)

    def shake_sort(self):
        temp = len(self.content) - 1

        left = 0
        right = temp

        while True:
            for i in range(left, right):
                if (self.content[i].quotient() > self.content[i+1].quotient()):
                    movie = self.content[i]

                    self.content[i] = self.content[i+1]
                    self.content[i+1] = movie

                    temp = i

            right = temp
            for i in range(right, left, -1):
                if (self.content[i].quotient() < self.content[i-1].quotient()):
                    movie = self.content[i]

                    self.content[i] = self.content[i-1]
                    self.content[i-1] = movie

                    temp = i

            left = temp

            if left >= right:
                break
