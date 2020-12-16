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

    correct = dict()
    # which rules are correct for which fields off all tickets
    for rnr, rule in enumerate(rules):
        for fnr in range(len(myticket)):
            for i, ticket in enumerate(tickets):
                if i in invalid:
                    continue
                if not rule.isvalid(ticket[fnr]):
                    break
            else:
                correct[rnr] = correct.get(rnr, set()) | {fnr}

    # Rule:Field
    taken = dict()
    prod = 1
    # check the rule with the least amount of validities for all tickets first
    # for this example this works but it is greedy and doesn't check all solutions
    for rnr in sorted(correct, key=lambda k: len(correct[k])):
        for available in correct[rnr]:
            if available not in taken.values():
                taken[rnr] = available
                if rules[rnr].name.startswith('departure'):
                    prod *= myticket[available]
    return prod


if __name__ == '__main__':
    data = parse_input('16.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
