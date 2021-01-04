
def parseValue(line, i):
    if line[i] == "(":
        # Stack
        print("Found a sub node", i)
        result, i = parseMath(line, i + 1)
        return result, i
    elif line[i] in ["+", "*", ")"]:
        raise Exception(line[i] + " is not expected to start a value")
    else:
        si = i
        while(i < len(line) and line[i] not in [" ", ")"]):
            i += 1

        return int(line[si:i]), i


def parseMath(line, i):

    # All math should start with a value
    lhs, i = parseValue(line, i)

    print("lhs", lhs)

    result = lhs
    # then optionally an operation followed by another value.
    while i < len(line):
        if line[i] == ")":
            # This is the end of this segment
            i += 1
            print("Completed sub node", i, result)
            break
        op = line[i + 1]
        print("op", op)

        val, i = parseValue(line, i + 3)
        print("math", result, op, val)

        if op == "*":
            result = result * val
        else:
            result = result + val

    return result, i

def part1():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        total = 0
        for line in lines:
            print(line)
            result, i = parseMath(line, 0)
            if i != len(line):
                print("i wasn't at the end of line???", i, len(line))
            print(result)
            total += result

        print("Part 1:", total)


def parseValue2(line, i):
    if line[i] == "(":
        # Stack
        print("Found a sub node", i)
        result, i = parseMath2(line, i + 1)
        return result, i
    elif line[i] in ["+", "*", ")"]:
        raise Exception(line[i] + " is not expected to start a value")
    else:
        si = i
        while(i < len(line) and line[i] not in [" ", ")"]):
            i += 1

        return int(line[si:i]), i


def parseSum2(line, i):

    # All math should start with a value
    lhs, i = parseValue2(line, i)

    print("lhs", lhs)

    result = lhs
    # then optionally an operation followed by another value.
    while i < len(line):
        if line[i] == ")":
            # This is the end of this segment
            print("Completed sum", i, result)
            break
        op = line[i + 1]
        print("op", op)
        if op == "*":
            print("Completed sum due to *", i, result)
            # The sum is completed
            break

        if op == "+":
            val, i = parseValue2(line, i + 3)
            print("add", result, op, val)
            result = result + val

    return result, i


def parseMath2(line, i):

    lhs, i = parseSum2(line, i)

    print("lhs", lhs)

    result = lhs
    # then optionally an operation followed by another value.
    while i < len(line):
        if line[i] == ")":
            # This is the end of this segment
            i += 1
            print("Completed sub node", i, result)
            break
        op = line[i + 1]
        print("op", op)

        if op == "*":
            val, i = parseSum2(line, i + 3)
            print("sum rhs math", result, op, val)
            result = result * val
        else:
            raise Exception("Unknown op " + op)

    return result, i


def part2():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        total = 0
        for line in lines:
            print(line)
            result, i = parseMath2(line, 0)
            if i != len(line):
                print("i wasn't at the end of line???", i, len(line))
            print(result)
            total += result

        print("Part 2:", total)


part1()
part2()
