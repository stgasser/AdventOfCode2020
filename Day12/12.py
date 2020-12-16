import numpy as np


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        return [(lines[0], int(lines[1:])) for lines in lines]


def rotate(x, ang):
    if ang < 0:
        ang += 360
    return x * 1j ** (ang / 90)


def part1(coordinates):
    absolute = {'N': 1, 'S': -1, 'E': 1j, 'W': -1j}
    relative = {'F': 1, 'B': -1, 'L': -1, 'R': 1}
    pos = 0
    heading = absolute['E']
    for cmd, n in coordinates:
        if cmd in absolute:
            pos += absolute[cmd] * n
        elif cmd in relative:
            if cmd == 'L' or cmd == 'R':
                heading = rotate(heading, n * relative[cmd])
            else:
                pos += heading * n * relative[cmd]
    return abs(pos.real) + abs(pos.imag)


def part2(coordinates):
    absolute = {'N': 1, 'S': -1, 'E': 1j, 'W': -1j}
    relative = {'F': 1, 'B': -1, 'L': -1, 'R': 1}
    pos = 0
    waypoint = 10 * absolute['E'] + 1 * absolute['N']
    for cmd, n in coordinates:
        if cmd in absolute:
            waypoint += absolute[cmd] * n
        elif cmd in relative:
            if cmd == 'L' or cmd == 'R':
                waypoint = rotate(waypoint, n * relative[cmd])
            else:
                pos += waypoint * n * relative[cmd]
    return abs(pos.real) + abs(pos.imag)


if __name__ == '__main__':
    data = parse_input('12.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
