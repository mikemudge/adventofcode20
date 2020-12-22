def parseSeat(v):
    r = v[:7]
    r = r.replace('B', '1')
    r = r.replace('F', '0')
    r = int(r, 2)

    c = v[7:]
    c = c.replace('R', '1')
    c = c.replace('L', '0')
    c = int(c, 2)

    i = r * 8 + c
    return i


def printSeat(v):
    s = parseSeat(v)
    print(s)
    return s


def part1():
    with open('input') as f:
        lines = f.readlines()

        ids = []
        for l in lines:
            l = l.rstrip()
            s = parseSeat(l)
            ids.append(s)

        print("Part 1:", max(ids))
        ids = sorted(ids)
        print(ids)

        lastx = ids[0] - 1
        for x in ids:
            if lastx + 1 != x:
                print("missing", lastx + 1)
                missing = lastx + 1
            lastx = x

        print("Part 2:", missing)




printSeat('BFFFBBFRRR')
printSeat('FFFBBBFRRR')
printSeat('BBFFBBFRLL')
part1()
