import numpy as np
from scipy.signal import convolve2d


def parse_input(filename):
    seats = np.loadtxt(filename, dtype=np.uint8, converters={0: lambda x: list(x)})
    return (seats == ord('L')).astype(int)


def part1(seats):
    occupied = np.zeros_like(seats)
    old = np.ones_like(seats)
    while not np.all(old == occupied):
        old = occupied.copy()
        freeadjacent = convolve2d(occupied == 0, np.ones((3, 3)), mode='same', fillvalue=1)
        occupiedneighbors = convolve2d(occupied, np.ones((3, 3)), mode='same', fillvalue=0)
        freeadjacent[seats == 0] = 0  # No one sits on the floor
        occupiedneighbors[seats == 0] = 0  # Safety
        occupied[freeadjacent == 9] = 1
        occupied[occupiedneighbors >= 5] = 0
    return occupied.sum()


def part2(seats):
    shape = np.array(seats.shape)
    neighbors = dict()
    for pos in np.argwhere(seats):
        neighbor_list = []
        for vel in np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]):
            new_pos = pos + vel
            while all(new_pos >= 0) and all(new_pos < shape) and seats[new_pos[0], new_pos[1]] == 0:
                new_pos += vel
            if all(new_pos >= 0) and all(new_pos < shape):
                neighbor_list += [tuple(new_pos)]
        neighbors[tuple(pos)] = tuple(zip(*neighbor_list))

    occupied = np.zeros_like(seats)
    old = np.ones_like(seats)

    while not np.all(old == occupied):
        old = occupied.copy()
        for idx in neighbors:
            see_occ = old[neighbors[idx]].sum()
            if see_occ >= 5:
                occupied[idx] = 0
            elif see_occ == 0:
                occupied[idx] = 1
    return occupied.sum()


if __name__ == '__main__':
    data = parse_input('11.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
