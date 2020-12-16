def parse_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def part1(lines):
    sol = []
    ans = set()
    for line in lines:
        if line == "":
            sol.append(len(ans))
            ans.clear()
        else:
            ans = ans | set(line)
    sol.append(len(ans))
    return sum(sol)


def part2(lines):
    sol = []
    ans = None
    for line in lines:
        if line == "":
            sol.append(len(ans))
            ans = None
        else:
            if ans is None:
                ans = set(line)
            else:
                ans = ans & set(line)
    sol.append(len(ans))
    return sum(sol)


if __name__ == '__main__':
    data = parse_input('6.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
