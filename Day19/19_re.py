import re
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


def gen(ruleid, rules):
    if type(rules[ruleid]) == str:
        return rules[ruleid]
    else:
        ret = []
        for rule_seq in rules[ruleid]:
            ret.append(''.join(gen(rule, rules) for rule in rule_seq))
        return '(' +'|'.join(ret)+')'


def part1(rules, msgs):
    cnt = 0
    pattern = gen(0, rules)
    prog = re.compile(pattern)
    for msg in msgs:
        if prog.fullmatch(msg):
            cnt += 1
    return cnt


def part2(rules, msgs):
    # since a^n b^n is not regular it cant be done with regex :-(
    thirtyone = re.compile(gen(31, rules))
    fortytwo = re.compile(gen(42, rules))
    cnt = 0
    for msg in msgs:
        tocnt = 0
        while thirtyone.fullmatch(msg[-8:]):
            tocnt += 1
            msg = msg[:-8]
        ftcnt = 0
        while len(msg) > 0 and fortytwo.fullmatch(msg[:8]):
            msg = msg[8:]
            ftcnt += 1
        if len(msg) == 0 and ftcnt - tocnt >= 1 and tocnt >= 1 and ftcnt >= 2:
            cnt += 1
    return cnt


if __name__ == '__main__':
    data = parse_input('19.in')
    print("Solution to part 1:", part1(*data))
    print("Solution to part 2:", part2(*data))