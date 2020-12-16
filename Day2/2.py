
def parse_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def part1(lines):
    valid = 0
    for line in lines:
        r, c, pw = line.split(' ')
        c = c[0]
        mi, ma = list(map(int, r.split('-')))
        occ = pw.count(c)
        if mi <= occ <= ma:
            valid += 1
    return valid


def part2(lines):
    valid = 0
    for line in lines:
        r, c, pw = line.split(' ')
        c = c[0]
        mi, ma = r.split('-')
        mi, ma = int(mi) - 1, int(ma) - 1
        # occ = pw.count(c)
        if (pw[mi] == c) ^ (pw[ma] == c):  # mi <= occ <= ma:
            # print(mi, occ, ma)
            valid += 1
    return valid


if __name__ == '__main__':
    data = parse_input('2.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
