def parse_input(filename):
    with open(filename) as f:
        return [list(line.replace(' ', '')) for line in f.read().splitlines()]


def part1(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        while len(eq) > 0:
            op = eq.pop(0)
            if op in {'+', '*'}:
                pass
            elif op == '(':
                evaluate(eq)
                continue
            elif op == ')':
                eq.insert(0, stack[0])
                return
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*':
                stack.append(stack.pop() * stack.pop())
            last = op
        return stack[0]
    return sum([evaluate(eq.copy()) for eq in equations])


def part2(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        while len(eq) > 0:
            op = eq.pop(0)
            if op in {'+', '*'}:
                pass
            elif op == '(':
                evaluate(eq)
                continue
            elif op == ')':
                if len(stack) == 2:
                    stack.insert(0, stack.pop(0) * stack.pop(0))  # finish last multiplikation
                eq.insert(0, stack[0])
                return
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*' and len(stack) > 2:  # can only multipy if 2 finished values on the stack
                stack.insert(0, stack.pop(0) * stack.pop(0))
            last = op
        if len(stack) == 2:
            stack.insert(0, stack.pop(0) * stack.pop(0))
        return stack[0]
    return sum([evaluate(eq.copy()) for eq in equations])


if __name__ == '__main__':
    data = parse_input('18.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
