from itertools import product
from collections import namedtuple

Mask = namedtuple('Mask', 'zeros ones float_indices')


def parse_line(line):
    cmd, val = line.split(' = ')
    if cmd == 'mask':
        return cmd, Mask(ones=int(val.replace('X', '0'), 2), zeros=int(val.replace('X', '1'), 2), float_indices=[i for i, c in enumerate(reversed(val)) if c == 'X'])
    else:
        return cmd, (int(cmd[4:-1]), int(val))


def parse_input(filename):
    with open(filename) as f:
        return [parse_line(line) for line in f.read().splitlines()]


def part1(commands):
    mem = dict()
    mask = Mask(ones=0, zeros=2**36 - 1, float_indices=[])
    for cmd, val in commands:
        if cmd == 'mask':
            mask = val
        elif cmd[:3] == 'mem':
            addr, val = val
            val |= mask.ones
            val &= mask.zeros
            mem[addr] = val
    return sum(mem.values())


def part2(commands):
    mask = Mask(ones=0, zeros=2**36 - 1, float_indices=[])
    mem = dict()
    for cmd, val in commands:
        if cmd == 'mask':
            mask = val
        elif cmd[:3] == 'mem':
            addr, val = val
            addr |= mask.ones
            for replacements in product('01', repeat=len(mask.float_indices)):
                a = addr
                for i, b in zip(mask.float_indices, replacements):
                    if b == '0':
                        a &= ~(1 << i)
                    else:
                        a |= 1 << i
                mem[a] = val
    return sum(mem.values())


if __name__ == '__main__':
    data = parse_input('14.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
