def parse_input(filename):
    with open(filename) as f:
        return [int(s) for s in f.readlines()]


def part1(numbers):
    for i in range(25, len(numbers)):
        for x in numbers[i - 25:i]:
            if numbers[i] - x in numbers[i - 25:i]:
                break
        else:
            return numbers[i]


def part2(numbers):
    invalid = part1(numbers)
    floor = 0
    ceil = 0
    cs = 0
    while ceil < len(numbers):
        if cs < invalid:
            cs += numbers[ceil]
            ceil += 1
        elif cs > invalid:
            cs -= numbers[floor]
            floor += 1
        else:
            return min(numbers[floor:ceil+1]) + max(numbers[floor:ceil+1])


if __name__ == '__main__':
    data = parse_input('9.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
