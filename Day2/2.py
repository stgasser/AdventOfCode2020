import numpy as np


def parse_input(filename):
    return set(np.loadtxt(filename, delimiter='\n', dtype=int))


def part1(numbers):
    for x in numbers:
        if 2020 - x in numbers:
            print(x, 2020 - x, x * (2020 - x))
            return


def part2(numbers):
    for x in numbers:
        for y in numbers:
            if x + y > 2020:
                continue
            if 2020 - x - y in numbers:
                print(x, y, 2020 - x - y, x * (2020 - x - y) * y)
                return


if __name__ == '__main__':
    data = parse_input('2.in')
    part1(data)
    part2(data)
