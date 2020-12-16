import numpy as np


class Rule:
    def __init__(self, s: str):
        self.name, ranges = s.strip().split(': ')
        self.ranges = [tuple(map(int, r.split('-'))) for r in ranges.split(' or ')]

    def isvalid(self, val: int):
        return any([mi <= val <= ma for mi, ma in self.ranges])


def parse_input(filename):
    with open(filename) as f:
        rs, mt, ts = f.read().split('\n\n')
        myticket = tuple(map(int, mt.splitlines()[-1].split(',')))
        tickets = [tuple(map(int, line.split(','))) for line in ts.splitlines()[1:]]
        rules = [Rule(s) for s in rs.splitlines()]
        return myticket, tickets, rules


def part1(args):
    myticket, tickets, rules = args
    errorrate = 0
    invalid = set()
    for i, ticket in enumerate(tickets):
        for field in ticket:
            for rule in rules:
                if rule.isvalid(field):
                    break
            else:
                errorrate += field
                invalid.add(i)
                break
    return errorrate


def part2(args):
    myticket, tickets, rules = args
    invalid = set()
    for i, ticket in enumerate(tickets):
        for field in ticket:
            for rule in rules:
                if rule.isvalid(field):
                    break
            else:
                invalid.add(i)
                break
    correct = np.zeros((len(myticket), len(rules)))
    for i, ticket in enumerate(tickets):
        if i in invalid:
            continue
        for fnr, field in enumerate(ticket):
            for rnr, rule in enumerate(rules):
                if rule.isvalid(field):
                    correct[fnr, rnr] += 1
    taken = dict()
    prod = 1
    for _, rnr in sorted([((correct[:, rnr] == len(tickets) - len(invalid)).sum(), rnr) for rnr in range(len(rules))]):
        for available in np.argwhere(correct[:, rnr] == len(tickets) - len(invalid)):
            if available[0] not in taken.values():
                taken[rnr] = available[0]
                if rules[rnr].name.startswith('departure'):
                    prod *= myticket[available[0]]
    return prod


if __name__ == '__main__':
    data = parse_input('16.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
