import inspect
import sys
import time

from utils import FileReader, FileWriter
from container import Container


def err_wrong_usage():
    print(inspect.cleandoc(
        """
        Incorrect usage.
          Expected:
            command -f input_file output_file_1 output_file_2
          Or:
            command -n size output_file_1 output_file_2
        """
    ))

    exit(1)


def err_wrong_qualifier():
    print(inspect.cleandoc(
        """
        Incorrect qualifier value.
          Expected:
            command -f input_file output_file_1 output_file_2
          Or:
            command -n size output_file_1 output_file_2
        """
    ))

    exit(1)


def err_wrong_file(filename: str):
    print("Incorrect file \"%s\" passed" % filename)
    exit(1)


def run():
    args = sys.argv

    if len(args) != 5:
        err_wrong_usage()

    if args[1] == "-f":
        run_file(args)
    elif args[1] == "-n":
        run_random(args)
    else:
        err_wrong_qualifier()


def run_file(args):
    container = Container()

    # Input
    container.input(open_file_read(args[2]))

    # Output (unsorted)
    container.output(open_file_write(args[3]))

    # Output (sorted)
    container.shake_sort()
    container.output(open_file_write(args[4]))


def run_random(args):
    container = Container()

    # Input
    container.input_random(args[2])

    # Output (unsorted)
    container.output(open_file_write(args[3]))

    # Output (sorted)
    container.shake_sort()
    container.output(open_file_write(args[4]))


def open_file_read(filename: str) -> FileReader:
    try:
        return FileReader(filename)
    except IOError:
        err_wrong_file(filename)


def open_file_write(filename: str) -> FileWriter:
    try:
        return FileWriter(filename)
    except IOError:
        err_wrong_file(filename)


if __name__ == "__main__":
    print("Start")
    start = time.process_time()

    run()

    stop = time.process_time()
    print("Stop")

    print("Time:", (stop - start), "sec")
