import argparse
from pathlib import Path

from exercise_1.exercise_1 import Exercise1


def write(file, text):
    with open(file, "w") as file:
        file.write(text)


def read(file):
    with open(file, "r") as file:
        return file.read()


def validate_file(file):
    if not Path(file).exists():
        raise ValueError("no such file")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use A* to search for optimal path in puzzle')
    parser.add_argument('in_file', type=str, help="File with problem puzzle")
    parser.add_argument('out_file', type=str, help='output file name')

    args = parser.parse_args()
    validate_file(args.in_file)

    write(args.out_file, Exercise1(read(args.in_file)).solution())
