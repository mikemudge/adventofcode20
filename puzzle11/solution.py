
def countAdjacent(lines, x, y, c):
    sum = 0
    if y > 0:
        if x > 0 and lines[y - 1][x - 1] == c:
            sum += 1
        if lines[y - 1][x] == c:
            sum += 1
        if x < len(lines[y - 1]) - 1 and lines[y - 1][x + 1] == c:
            sum += 1
    if x > 0 and lines[y][x - 1] == c:
        sum += 1
    if x < len(lines[y]) - 1 and lines[y][x + 1] == c:
        sum += 1
    if y < len(lines) - 1:
        if x > 0 and lines[y + 1][x - 1] == c:
            sum += 1
        if lines[y + 1][x] == c:
            sum += 1
        if x < len(lines[y + 1]) - 1 and lines[y + 1][x + 1] == c:
            sum += 1
    return sum

def iterate(lines):
    next = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            res = lines[y][x]
            if lines[y][x] == "L":
                if countAdjacent(lines, x, y, "#") == 0:
                    res = "#"
            if lines[y][x] == "#":
                if countAdjacent(lines, x, y, "#") >= 4:
                    res = "L"
            row.append(res)
        next.append(row)
    return next


def countGrid(lines):
    return sum([sum([let == "#" for let in line]) for line in lines])


def printGrid(lines):
    print("\n".join(["".join([let for let in line]) for line in lines]))


def part1():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        printGrid(lines)
        for i in range(100000):
            next = iterate(lines)
            print("Round %d" % i)
            printGrid(next)
            print(countGrid(next))
            if lines == next:
                break
            lines = next

def checkSeat(lines, x, y, dx, dy, c):
    while(True):
        x += dx
        y += dy
        if y < 0:
            break
        if y >= len(lines):
            break
        if x < 0:
            break
        if x >= len(lines[0]):
            break
        if lines[y][x] != '.':
            return lines[y][x] == c
    return False


def countDirection2(lines, x, y, c):
    sum = 0
    if checkSeat(lines, x, y, -1, -1, c):
        sum += 1
    if checkSeat(lines, x, y, 0, -1, c):
        sum += 1
    if checkSeat(lines, x, y, 1, -1, c):
        sum += 1
    if checkSeat(lines, x, y, -1, 0, c):
        sum += 1
    if checkSeat(lines, x, y, 1, 0, c):
        sum += 1
    if checkSeat(lines, x, y, -1, 1, c):
        sum += 1
    if checkSeat(lines, x, y, 0, 1, c):
        sum += 1
    if checkSeat(lines, x, y, 1, 1, c):
        sum += 1
    return sum


def iterate2(lines):
    next = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            res = lines[y][x]
            if lines[y][x] == "L":
                if countDirection2(lines, x, y, "#") == 0:
                    res = "#"
            if lines[y][x] == "#":
                if countDirection2(lines, x, y, "#") >= 5:
                    res = "L"
            row.append(res)
        next.append(row)
    return next


def part2():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        printGrid(lines)
        for i in range(100000):
            next = iterate2(lines)
            print("Round %d" % i)
            printGrid(next)
            print(countGrid(next))
            if lines == next:
                break
            lines = next

part1()
part2()