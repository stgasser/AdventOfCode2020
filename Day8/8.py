class Program:
    def __init__(self, code):
        self.pc = 0
        self.code = code
        self.acc = 0
        self.hist = set()

    def execute(self):
        while self.pc < len(self.code):
            if self.pc in self.hist:
                return
            if self.pc < 0:
                print("WTF")
                return
            self.hist.add(self.pc)
            ins, args = self.code[self.pc]
            if ins == 'jmp':
                self.pc += args
            else:
                if ins == 'acc':
                    self.acc += args
                elif ins == 'nop':
                    pass
                else:
                    print('Error Unknown Instruction', ins, args)
                self.pc += 1
        return self.acc


def parse_instruction(inst):
    sa = inst.split(" ")
    return sa[0], int(sa[1])


def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        return [parse_instruction(line) for line in lines]


def part1(code):
    prog = Program(code.copy())
    prog.execute()
    return prog.acc


def part2(code):
    for i in range(len(code)):
        if code[i][0] == 'acc':
            continue
        temp = code.copy()
        temp[i] = 'nop' if temp[i][0] == 'jmp' else 'jmp', temp[i][1]
        prog = Program(temp)
        ret = prog.execute()
        if ret is not None:
            return ret


if __name__ == '__main__':
    data = parse_input('8.in')
    print("Solution to part 1:", part1(data))
    print("Solution to part 2:", part2(data))
