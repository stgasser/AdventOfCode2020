def parse_input(filename):
    with open(filename) as f:
        return list(map(int, f.read()))


def part1(cups):    # Noob solution
    idx = 0
    mi, ma = min(cups), max(cups)
    for _ in range(100):
        curcup = cups[idx]
        pickup = (cups[idx + 1:] + cups[:idx])[:3]
        dest = curcup - 1
        while dest not in cups or dest in pickup:
            dest -= 1
            if dest < mi:
                dest = ma
        for i, n in enumerate(pickup):
            cups.pop(cups.index(n))
            cups.insert(cups.index(dest) + i + 1, n)
        idx = cups.index(curcup) + 1
        idx %= len(cups)
    idx = cups.index(1)
    return ''.join(map(str, cups[idx + 1:] + cups[:idx]))


def part2(cups, cupcnt=10**6, itercnt=10**7):    # Solution using array as self linked list
    circle = [0, ] * (cupcnt + 1)    # Using numpy arrays or array arrays is not fast in this case
    for i in range(len(cups) + 1, cupcnt):
        circle[i] = i + 1
    for i in range(len(cups)-1):
        circle[cups[i]] = cups[i + 1]
    circle[cups[-1]] = len(cups) + 1
    circle[-1] = cups[0]
    curcup = cups[0]
    pickups = [0, 0, 0]
    for e in range(itercnt):
        curr = circle[curcup]
        for i in range(3):
            pickups[i] = curr
            curr = circle[curr]
        circle[curcup] = curr
        dest = curcup
        while dest == curcup or dest in pickups:
            dest -= 1
            if dest == 0:
                dest = cupcnt
        circle[pickups[-1]] = circle[dest]
        circle[dest] = pickups[0]
        curcup = circle[curcup]
    return circle[1] * circle[circle[1]]


if __name__ == '__main__':
    data = parse_input('23.in')
    print("Solution to part 1:", part1(data.copy()))
    print("Solution to part 2:", part2(data.copy()))
