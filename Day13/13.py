def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        return int(lines[0]), [(i, int(b)) for i, b in enumerate(lines[1].split(',')) if b != 'x']


def part1(timestamp, busses):
    _, b = min(busses, key=lambda bus: (bus[1] - timestamp % bus[1]))
    return b * (b - timestamp % b)


def part2(timestamp, busses):
    curr = 0
    found = 0
    adv = 1
    dt, bus = busses[found]
    while True:
        curr += adv
        if (curr + dt) % bus == 0:
            adv *= bus
            found += 1
            if found == len(busses):
                break
            dt, bus = busses[found]
    return curr


if __name__ == '__main__':
    data = parse_input('13.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))
