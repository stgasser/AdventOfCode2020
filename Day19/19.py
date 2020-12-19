from itertools import product


def parse_input(filename):
    with open(filename) as f:
        rules_txt, msgs_txt = f.read().split("\n\n")
        rules = dict()
        for line in rules_txt.splitlines():
            idx, rule = line.split(': ')
            idx = int(idx)
            if '"' in rule:
                rule = rule[1]
            else:
                rule = [list(map(int, r.split(' '))) for r in rule.split(' | ')]
            rules[idx] = rule
        return rules, msgs_txt.splitlines()


def gen(rule, rules):
    if type(rule) == str:
        return set(rule)
    else:
        ret = set()
        for rule_seq in rule:
            tmp = tuple(gen(rules[r], rules) for r in rule_seq)
            ret = ret | set(''.join(tpl) for tpl in product(*tmp))
        return ret


def part1(rules, msgs):
    cnt = 0
    possible_msgs = gen(rules[0], rules)
    for msg in msgs:
        if msg in possible_msgs:
            cnt += 1
    return cnt


def part2(rules, msgs):
    thirtyone = gen(rules[31], rules)  # luckily mutually exclusive
    fortytwo = gen(rules[42], rules)
    cnt = 0
    for msg in msgs:
        tocnt = 0
        while msg[-8:] in thirtyone:
            tocnt += 1
            msg = msg[:-8]
        ftcnt = 0
        while len(msg) > 0 and msg[:8] in fortytwo:
            msg = msg[8:]
            ftcnt += 1
        if len(msg) == 0 and ftcnt - tocnt >= 1 and tocnt >= 1 and ftcnt >= 2:
            cnt += 1
    return cnt


if __name__ == '__main__':
    data = parse_input('19.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))
