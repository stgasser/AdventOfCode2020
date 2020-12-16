import numpy as np


def parse_input(filename):
    return np.loadtxt(filename, dtype=np.byte, comments="-", converters={0: lambda x: list(x)}) == ord('#')


def part1(field, velocity=(1, 3)):
    pos = np.array([0, 0])
    vel = np.array(velocity)
    trees = 0
    pos += vel
    while pos[0] < field.shape[0]:
        if field[pos[0], pos[1] % field.shape[1]]:
            trees += 1
        pos += vel
    return trees


def part2(field):
    overall = 1
    for velocity in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        overall *= part1(field, velocity=velocity)
    return overall


if __name__ == '__main__':
    data = parse_input('3.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
