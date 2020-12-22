def parse_input(filename):
    with open(filename) as f:
        p1, p2 = f.read().split('\n\n')
        return list(map(int, p1.splitlines()[1:])), list(map(int, p2.splitlines()[1:]))


def part1(d1, d2):
    p1, p2 = d1.copy(), d2.copy()
    while len(p1) > 0 and len(p2) > 0:
        c1, c2 = p1.pop(0), p2.pop(0)
        if c1 > c2:
            p1 += [c1, c2]
        elif c2 > c1:
            p2 += [c2, c1]
    win = p1 if len(p1) > 0 else p2
    return sum([c * (i + 1) for c, i in zip(reversed(win), range(len(win)))])


def part2(d1, d2):
    def recursive_combat(p1, p2):
        hist = set()
        while len(p1) > 0 and len(p2) > 0:
            cur_state = (tuple(p1), tuple(p2))
            if cur_state in hist:
                return True, p1
            hist.add(cur_state)
            c1, c2 = p1.pop(0), p2.pop(0)
            if c1 <= len(p1) and c2 <= len(p2):
                p1win, _ = recursive_combat(p1[:c1].copy(), p2[:c2].copy())
            else:
                p1win = c1 > c2
            if p1win:
                p1 += [c1, c2]
            else:
                p2 += [c2, c1]
        # if p1 won round and game is over p1 must have won overall
        return p1win, p1 if p1win else p2

    _, win = recursive_combat(d1.copy(), d2.copy())
    return sum([c * (i + 1) for c, i in zip(reversed(win), range(len(win)))])


if __name__ == '__main__':
    data = parse_input('22.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))
