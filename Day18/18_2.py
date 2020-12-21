def parse_input(filename):
    with open(filename) as f:
        return [line.replace(' ', '') for line in f.read().splitlines()]


def part1(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        op = next(eq, None)
        while op is not None:
            if op in {'+', '*'}:
                pass
            elif op == '(':
                op = evaluate(eq)
                continue
            elif op == ')':
                break
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*':
                stack.append(stack.pop() * stack.pop())
            last = op
            op = next(eq, None)
        return stack[0]

    return sum([evaluate(iter(eq)) for eq in equations])


def part2(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        op = next(eq, None)
        while op is not None:
            if op in {'+', '*'}:
                pass
            elif op == '(':
                op = evaluate(eq)
                continue
            elif op == ')':
                break
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*' and len(stack) > 2:  # can only multiply if 2 finished values on the stack
                stack.insert(0, stack.pop(0) * stack.pop(0))
            last = op
            op = next(eq, None)
        if len(stack) == 2:
            stack.insert(0, stack.pop(0) * stack.pop(0))
        return stack[0]

    return sum([evaluate(iter(eq)) for eq in equations])


if __name__ == '__main__':
    data = parse_input('18.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
