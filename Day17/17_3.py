import numpy as np
from scipy.ndimage.filters import convolve


def parse_input(filename):
    seats = np.loadtxt(filename, dtype=np.uint8, converters={0: lambda x: list(x)}, comments='-')
    return seats == ord('#')


def part1(initial, dim=3):
    kernel = np.ones((3,) * dim, dtype=int)
    kernel[(1,) * dim] = 0
    cubes = initial.copy().reshape((1,) * (dim - len(initial.shape)) + initial.shape).astype(int)
    for _ in range(6):
        cubes = np.pad(cubes, 1)
        neighbors = convolve(cubes, kernel, mode='wrap')
        cubes = (((cubes == 1) & ((neighbors == 2) | (neighbors == 3))) + ((cubes == 0) & (neighbors == 3))).astype(int)
    return cubes.sum()


def part2(initial):
    return part1(initial, dim=4)


if __name__ == '__main__':
    data = parse_input('17.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
