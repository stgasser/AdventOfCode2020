def part1(preamble, end=2020):
    last = -1
    spoken = dict()
    for i in range(0, end):
        if i < len(preamble):
            new_number = preamble[i]
        elif last in spoken:
            new_number = i - spoken[last]
        else:
            new_number = 0
        if i > 0:
            spoken[last] = i
        last = new_number
    return last


def part2(preamble):
    return part1(preamble, end=30000000)


if __name__ == '__main__':
    data = [7, 12, 1, 0, 16, 2]
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
