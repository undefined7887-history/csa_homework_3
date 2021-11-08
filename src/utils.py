import random
import string
from typing import IO


def rand_string(length: int):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))


def rand_int(min: int, max: int):
    return random.randint(min, max)


class FileReader:
    def __init__(self, filename: str) -> None:
        self.values = []
        self.file = open(filename, "r")

    def __request_values(self) -> bool:
        if len(self.values) > 0:
            return True

        try:
            self.values.extend(
                filter(None, self.file.readline().strip().split(" "))
            )

            return len(self.values) > 0
        except IOError:
            return False

    def read_int(self) -> int:
        if self.__request_values():
            try:
                return int(self.values.pop(0))
            except ValueError:
                return 0

    def read_string(self) -> str:
        if self.__request_values():
            return self.values.pop(0)

    def has_next(self) -> bool:
        return self.__request_values()


class FileWriter:
    def __init__(self, filename: str) -> None:
        self.file = open(filename, "w+")

    def write(self, data: str) -> None:
        self.file.write(data)

    def write_line(self, data: str) -> None:
        self.write(data)
        self.file.write("\n")
