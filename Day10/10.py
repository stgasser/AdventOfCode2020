def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        adapters = [int(s) for s in lines]
        adapters += [0, max(adapters) + 3]
        return sorted(adapters)


def part1(adapters):
    diffs = dict()
    for a, b in zip(adapters, adapters[1:]):
        diffs[b - a] = diffs.get(b - a, 0) + 1
    return diffs[1] * diffs[3]


def perms(n):
    if n < 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return perms(n - 1) + perms(n - 2) + perms(n - 3)


def part2(adapters):
    comb = 1
    n = 1
    for a, b in zip(adapters, adapters[1:]):
        if b - a == 3:
            comb *= perms(n)
            n = 1
        elif b - a == 1:
            n += 1
        else:
            print(b - a)
    return comb


if __name__ == '__main__':
    data = parse_input('10.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
