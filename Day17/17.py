import numpy as np
from itertools import product


def parse_input(filename):
    seats = np.loadtxt(filename, dtype=np.uint8, converters={0: lambda x: list(x)}, comments='-')
    return seats == ord('#')


def get_neighbors(pos):
    for ds in product([1, 0, -1], repeat=len(pos)):
        # skip if all 0's
        if not any(ds):
            continue
        yield tuple(c + d for c, d in zip(pos, ds))


def part1(initial):
    cubes = {(pos[0], pos[1], 0) for pos in np.argwhere(initial)}
    for _ in range(6):
        visited = set()
        fringe = cubes.copy()
        new_cubes = set()
        while fringe:
            pos = fringe.pop()
            if pos in visited:
                continue
            visited.add(pos)
            neighbors = 0
            for new_pos in get_neighbors(pos):
                if new_pos in cubes:
                    neighbors += 1
                if pos in cubes:
                    fringe.add(new_pos)
            if 2 <= neighbors <= 3 and pos in cubes or neighbors == 3 and pos not in cubes:
                new_cubes.add(pos)
        cubes = new_cubes
    return len(cubes)


def part2(initial):
    cubes = {(pos[0], pos[1], 0, 0) for pos in np.argwhere(initial)}
    for _ in range(6):
        visited = set()
        fringe = cubes.copy()
        new_cubes = set()
        while fringe:
            pos = fringe.pop()
            if pos in visited:
                continue
            visited.add(pos)
            neighbors = 0
            for new_pos in get_neighbors(pos):
                if new_pos in cubes:
                    neighbors += 1
                if pos in cubes:
                    fringe.add(new_pos)
            if 2 <= neighbors <= 3 and pos in cubes or neighbors == 3 and pos not in cubes:
                new_cubes.add(pos)
        cubes = new_cubes
    return len(cubes)


if __name__ == '__main__':
    data = parse_input('17.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
