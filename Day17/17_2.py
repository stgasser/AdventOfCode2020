import numpy as np
from itertools import product
from collections import Counter


def parse_input(filename):
    seats = np.loadtxt(filename, dtype=np.uint8, converters={0: lambda x: list(x)}, comments='-')
    return seats == ord('#')


def get_dir(dim):
    for ds in product([1, 0, -1], repeat=dim):
        if not any(ds):
            continue
        yield ds


def part1(initial, dim=3):
    cubes = {(pos[0], pos[1]) + (1,) * (dim - len(pos)) for pos in np.argwhere(initial)}
    dirs = set(get_dir(dim))
    for _ in range(6):
        neighbor_cnt = Counter(tuple(c + d for c, d in zip(pos, ds)) for pos in cubes for ds in dirs)
        new_cubes = {pos for pos, neighbors in neighbor_cnt.items() if neighbors == 3 and pos} - cubes
        cubes = new_cubes | {pos for pos in cubes if neighbor_cnt[pos] == 2 or neighbor_cnt[pos] == 3}
    return len(cubes)


def part2(initial):
    return part1(initial, dim=4)


if __name__ == '__main__':
    data = parse_input('17.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
