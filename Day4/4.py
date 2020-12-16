def parse_input(filename):
    with open(filename) as f:
        passports = []
        curr = []
        for line in f.read().splitlines():
            if line == "":
                passports.append(" ".join(curr))
                curr.clear()
            else:
                curr.append(line)
        passports.append(" ".join(curr))
        return passports


def part1(passports):
    req = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
    valid = 0
    for pp in passports:
        keys = set()
        for field in pp.split(' '):
            k, _ = field.split(':')
            keys.add(k)
        if keys >= req:
            # print(pp)
            valid += 1
    return valid


def part2(passports):
    req = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}  # 'cid',
    ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    validators = {'byr': lambda s: len(s) == 4 and (1920 <= int(s) <= 2002),
                  'ecl': lambda s: s in ecls,
                  'eyr': lambda s: len(s) == 4 and (2020 <= int(s) <= 2030),
                  'hcl': lambda s: s[0] == '#' and len(s) == 7 and min(['a' <= c <= 'f' or '0' <= c <= '9' for c in s[1:]]),
                  'hgt': lambda s: s[-2:] == 'cm' and 150 <= int(s[:-2]) <= 193 or s[-2:] == 'in' and 59 <= int(s[:-2]) <= 76,
                  'iyr': lambda s: len(s) == 4 and (2010 <= int(s) <= 2020),
                  'pid': lambda s: len(s) == 9 and min(['0' <= c <= '9' for c in s]),
                  'cid': lambda _: True}
    valid = 0
    for pp in passports:
        keys = set()
        for field in pp.split(' '):
            k, v = field.split(':')
            if validators[k](v):
                # print(k,v)
                keys.add(k)
        if keys >= req:
            # print(pp)
            valid += 1
    return valid


if __name__ == '__main__':
    data = parse_input('4.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
