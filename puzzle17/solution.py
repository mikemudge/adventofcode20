import math

class Grid(object):

    def __init__(self, lines):
        self.lines = lines

    def get(self, x, y):
        if y < 0 or y >= len(self.lines):
            return False
        if x < 0 or x >= len(self.lines[y]):
            return False
        return self.lines[y][x]

    def countNeighbours(self, x, y):
        sum = 0
        if self.get(x - 1, y - 1):
            sum += 1
        if self.get(x, y - 1):
            sum += 1
        if self.get(x + 1, y - 1):
            sum += 1
        if self.get(x - 1, y):
            sum += 1
        if self.get(x, y):
            sum += 1
        if self.get(x + 1, y):
            sum += 1
        if self.get(x - 1, y + 1):
            sum += 1
        if self.get(x, y + 1):
            sum += 1
        if self.get(x + 1, y + 1):
            sum += 1
        return sum

    def getActiveCount(self):
        return sum([sum(x) for x in self.lines])

    def __str__(self):
        return "\n".join(["".join(["#" if x else "." for x in l]) for l in self.lines])


EMPTY = Grid([])


def calculateState(under, middle, above):
    result = []

    if len(under.lines):
        xsize = len(under.lines[0])
    elif len(above.lines):
        xsize = len(above.lines[0])
    else:
        xsize = len(middle.lines[0])

    if len(under.lines):
        ysize = len(under.lines)
    elif len(above.lines):
        ysize = len(above.lines)
    else:
        ysize = len(middle.lines)

    for y in range(0, ysize + 2):
        row = []
        for x in range(0, xsize + 2):
            # Increment based on surrounds.
            wasOn = middle.get(x - 1, y - 1)
            c = middle.countNeighbours(x - 1, y - 1)
            if wasOn:
                # Would of counted self as a neighbour.
                c -= 1
            c += under.countNeighbours(x - 1, y - 1)
            c += above.countNeighbours(x - 1, y - 1)

            v = c == 3 or (c == 2 and wasOn)
            row.append(v)
        result.append(row)

    return Grid(result)


def iterate(cube):

    results = []
    for i in range(0, len(cube) + 2):
        a = cube[i - 2] if i - 2 >= 0 else EMPTY
        b = cube[i - 1] if 0 <= i - 1 < len(cube) else EMPTY
        c = cube[i] if i < len(cube) else EMPTY

        results.append(calculateState(a, b, c))
    return results


def part1():
    with open('input') as f:
        lines = f.readlines()

        lines = [[x == "#" for x in l.rstrip()] for l in lines]

        g = Grid(lines)

        print("Cycle 0")
        print(g)
        print(g.getActiveCount())

        results = [[EMPTY]] * 7
        results[0] = [g]
        for i in range(1, 7):
            print ("Cycle %d" % i)
            r = iterate(results[i - 1])
            half = math.floor(len(r) / 2.0)
            for z, grid in enumerate(r):
                print("z = %d" % (z - half))
                # print(grid)

            results[i] = r

        active = 0
        for g in results[6]:
            active += g.getActiveCount()
        print("Part 1:", active)


def getNeighbourGrid(gridOfGrids, w, z):
    grid = gridOfGrids.get(w, z)
    if not grid:
        return EMPTY
    return grid


def part2():
    with open('input') as f:
        lines = f.readlines()

        lines = [[x == "#" for x in l.rstrip()] for l in lines]

        g = Grid(lines)

        print("Cycle 0")
        print(g)
        print(g.getActiveCount())

        results = [EMPTY] * 7
        results[0] = Grid([[g]])
        for i in range(1, 7):
            print ("Cycle %d" % i)

            last = results[i - 1]
            grid = last.lines[0][0]
            ysize = len(grid.lines)
            xsize = len(grid.lines[0])
            gridArray = []
            for z in range(0, len(last.lines) + 2):
                row2 = []
                for w in range(0, len(last.lines[0]) + 2):
                    middle = getNeighbourGrid(last, w - 1, z - 1)

                    result = []
                    for y in range(0, ysize + 2):
                        row = []
                        for x in range(0, xsize + 2):
                            wasOn = middle.get(x - 1, y - 1)
                            activeNeighbours = middle.countNeighbours(x - 1, y - 1)
                            if wasOn:
                                # Would have counted self.
                                activeNeighbours -= 1
                            activeNeighbours += getNeighbourGrid(last, w - 2, z - 2).countNeighbours(x - 1, y - 1)
                            activeNeighbours += getNeighbourGrid(last, w - 1, z - 2).countNeighbours(x - 1, y - 1)
                            activeNeighbours += getNeighbourGrid(last, w, z - 2).countNeighbours(x - 1, y - 1)

                            activeNeighbours += getNeighbourGrid(last, w - 2, z - 1).countNeighbours(x - 1, y - 1)
                            activeNeighbours += getNeighbourGrid(last, w, z - 1).countNeighbours(x - 1, y - 1)

                            activeNeighbours += getNeighbourGrid(last, w - 2, z).countNeighbours(x - 1, y - 1)
                            activeNeighbours += getNeighbourGrid(last, w - 1, z).countNeighbours(x - 1, y - 1)
                            activeNeighbours += getNeighbourGrid(last, w, z).countNeighbours(x - 1, y - 1)

                            v = activeNeighbours == 3 or (activeNeighbours == 2 and wasOn)
                            row.append(v)
                        result.append(row)

                    row2.append(Grid(result))
                gridArray.append(row2)
            r = Grid(gridArray)

            half = math.floor(len(r.lines) / 2.0)
            for z in range(0, len(r.lines)):
                for w in range(0, len(r.lines[0])):
                    grid = r.get(w, z)
                    if i < 2:
                        print("z = %d, w = %d" % ((z - half), (w - half)))
                        print(grid)

            results[i] = r

        active = 0
        r = results[6]
        for z in range(0, len(r.lines)):
            for w in range(0, len(r.lines[0])):
                g = r.get(w, z)
                active += g.getActiveCount()
        print("Part 1:", active)


part1()
part2()