def parse_input(filename):
    with open(filename) as f:
        return [int(line.translate({ord(k): ord(v) for k, v in {'L': '0', 'R': '1', 'F': '0', 'B': '1'}.items()}), 2) for line in f.read().splitlines()]


def part1(seats):
    return max(seats)


def part2(seats):
    seats = set(seats)
    for i in set(range(2 ** 10)) - seats:
        if i + 1 in seats and i - 1 in seats:
            return i


if __name__ == '__main__':
    data = parse_input('5.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
