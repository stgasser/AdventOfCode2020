def parse_input(filename):
    with open(filename) as f:
        return [list(line.replace(' ', '')) for line in f.read().splitlines()]


def part1(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        i = 0
        while i < len(eq):
            op = eq[i]
            if op in {'+', '*'}:
                pass
            elif op == '(':
                bcnt = 1
                j = i + 1
                while bcnt > 0:
                    if eq[j] == '(':
                        bcnt += 1
                    elif eq[j] == ')':
                        bcnt -= 1
                    j += 1
                j -= 1
                stack.append(evaluate(eq[i + 1:j]))
                i = j
            elif op == ')':
                raise NotImplementedError('Should never go here')
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*':
                stack.append(stack.pop() * stack.pop())
            last = op
            i += 1
        return stack[0]

    return sum([evaluate(eq.copy()) for eq in equations])


def part2(equations):
    def evaluate(eq):
        stack = list()
        last = ''
        i = 0
        while i < len(eq):
            op = eq[i]
            if op in {'+', '*'}:
                pass
            elif op == '(':
                bcnt = 1
                j = i + 1
                while bcnt > 0:
                    if eq[j] == '(':
                        bcnt += 1
                    elif eq[j] == ')':
                        bcnt -= 1
                    j += 1
                j -= 1
                stack.append(evaluate(eq[i + 1:j]))
                i = j
            elif op == ')':
                raise NotImplementedError('Should never go here')
            else:
                stack.append(int(op))
            if last == '+':
                stack.append(stack.pop() + stack.pop())
            elif last == '*' and len(stack) > 2:  # can only multipy if 2 finished values on the stack
                stack.insert(0, stack.pop(0) * stack.pop(0))
            last = op
            i += 1
        if len(stack) == 2:
            stack.insert(0, stack.pop(0) * stack.pop(0))
        return stack[0]

    return sum([evaluate(eq.copy()) for eq in equations])


if __name__ == '__main__':
    data = parse_input('18.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
