
def parseLocation(line):
    x = 0
    y = 0
    z = 0
    i = 0
    while i < len(line):
        d = line[i]
        if d in ['s', 'n']:
            # increment i and add the next char to d
            # supports se, ne, sw and nw
            i += 1
            d += line[i]

        # print(i, line[i], d)

        if d == 'e':
            x += 1
            y -= 1
        elif d == 'w':
            x -= 1
            y += 1
        elif d == 'ne':
            x += 1
            z -= 1
        elif d == 'se':
            y -= 1
            z += 1
        elif d == 'nw':
            y += 1
            z -= 1
        elif d == 'sw':
            x -= 1
            z += 1
        else:
            raise Exception("direction (%s) is unknown, %s at %d" % (d, line[i], i))
        i += 1
    return x, y, z

def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        flips = {}
        for line in lines:
            loc = parseLocation(line)
            print("Ended at ", loc)
            if loc not in flips:
                flips[loc] = 0
            flips[loc] += 1

        blackTiles = 0
        for loc, f in flips.items():
            if f % 2 == 1:
                blackTiles += 1

        print("Part 1:", blackTiles)

def neighbours(loc):
    return [
        (loc[0], loc[1] - 1, loc[2] + 1),
        (loc[0], loc[1] + 1, loc[2] - 1),
        (loc[0] - 1, loc[1] + 1, loc[2]),
        (loc[0] + 1, loc[1] - 1, loc[2]),
        (loc[0] - 1, loc[1], loc[2] + 1),
        (loc[0] + 1, loc[1], loc[2] - 1)
    ]

def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        flips = {}
        for line in lines:
            loc = parseLocation(line)
            print("Ended at ", loc)
            if loc not in flips:
                flips[loc] = 0
            flips[loc] += 1

        initialPattern = {}
        blackTiles = 0
        for loc, f in flips.items():
            print(loc, f)
            if f % 2 == 1:
                blackTiles += 1
                initialPattern[loc] = True

        pattern = initialPattern
        days = 100
        for day in range(days + 1):
            if day != 0:
                print("Day %d" % day, blackTiles)

            neighbourCount = {}
            for loc in pattern:
                # count each neighbour as having this tile next to it.
                for n in neighbours(loc):
                    if n not in neighbourCount:
                        neighbourCount[n] = 0
                    neighbourCount[n] += 1

            blackTiles = 0
            nextPattern = {}
            for loc, n in neighbourCount.items():
                if n == 2:
                    nextPattern[loc] = True
                    blackTiles += 1
                elif n == 1 and loc in pattern:
                    # If the tile has 1 black tile adjacent and was already black, stay black.
                    nextPattern[loc] = True
                    blackTiles += 1
                # Otherwise it will be white, and excluded from the nextPattern.
            pattern = nextPattern
part1()
part2()
