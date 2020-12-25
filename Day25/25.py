def parse_input(filename):
    with open('25.in') as f:
        pub1, pub2 = f.read().splitlines()
        return int(pub1), int(pub2)


def part1(pub1, pub2):
    sn = 7
    cv = 1
    cnt = 0
    while True:
        if cv == pub1:
            ls = cnt
            cv = 1
            sn = pub2
            break
        if cv == pub2:
            ls = cnt
            cv = 1
            sn = pub1
            break
        cv = cv * sn
        cv = cv % 20201227
        cnt += 1
    for _ in range(ls):
        cv = cv * sn
        cv = cv % 20201227
    return cv


def part2(pub1, pub2):
    pass


if __name__ == '__main__':
    data = parse_input('2.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))
