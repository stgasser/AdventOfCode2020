import numpy as np


def parse_input(filename):
    return set(np.loadtxt(filename, delimiter='\n', dtype=int))


def part1(numbers):
    for x in numbers:
        if 2020 - x in numbers:
            return x * (2020 - x)


def part2(numbers):
    for x in numbers:
        for y in numbers:
            if x + y > 2020:
                continue
            if 2020 - x - y in numbers:
                return x * (2020 - x - y) * y


if __name__ == '__main__':
    data = parse_input('1.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
