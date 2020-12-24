
class Computer(object):

    def __init__(self, instructions):
        self.instructions = instructions
        self.pointer = 0
        self.accumulator = 0
        self.verbose = False
        self.terminated = False

    def runOne(self):
        if self.pointer == len(self.instructions):
            # Reached the end of the instructions.
            self.terminated = True
            return
        next = self.instructions[self.pointer]
        self.execute(next)

    def execute(self, instruction):
        op, val = instruction.split(" ")
        val = int(val)
        if self.verbose:
            print("run", self.pointer, op, val, self.accumulator)
        if op == 'acc':
            self.accumulator += val
        elif op == 'jmp':
            self.pointer += val
            # Skip the pointer increment for jumps
            return
        elif op == 'nop':
            pass
        else:
            raise Exception("Unknown op %s" % op)

        self.pointer += 1

def part1():
    with open('input') as f:
        lines = f.readlines()

        c = Computer(lines)

        visited = {}
        while c.pointer not in visited:
            visited[c.pointer] = True
            c.runOne()

        print(c.pointer, c.accumulator)


def part2():
    with open('input') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            op, val = line.split(" ")
            val = int(val)
            lines2 = lines[:]
            if line[:3] == "jmp":
                lines2[i] = "nop %d" % val
            elif line[:3] == "nop":
                lines2[i] = "jmp %d" % val
            else:
                # skip over lines which are not jmp or nop
                continue

            c = Computer(lines2)

            visited = {}
            while c.pointer not in visited:
                visited[c.pointer] = True
                c.runOne()
                if c.terminated:
                    print("Success run with %d modified" % i, c.pointer, c.accumulator)


            print("Finished run with %d modified" % i, c.pointer, c.accumulator)
            # 1176 was too high.

part2()