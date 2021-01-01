
def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        t = int(lines[0])
        busIds = lines[1].split(",")
        numbers = []
        for x in busIds:
            if x == "x":
                continue
            numbers.append(int(x))

        print(t)
        print(numbers)

        waits = {}
        for busId in numbers:
            d = t / busId
            r = t % busId
            print(busId, d, r, d * busId, (d + 1) * busId, (d + 1) * busId - t)
            waits[busId] = (d + 1) * busId - t

        s = sorted(waits.items(), key=lambda x: x[1])
        print(s)
        shortestWait = s[0]
        print("Part1", shortestWait, shortestWait[0] * shortestWait[1])


def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        busIds = lines[1].split(",")
        busTimes = {}
        for i, busId in enumerate(busIds):
            if busId == "x":
                continue
            busTimes[busId] = i

        print(busTimes)
        baseT = 0
        incrT = 1
        for busId in busTimes:
            busFreq = int(busId)
            offset = busTimes[busId]
            print("Current state", baseT, incrT)
            print("Adding new bus", "every %s minutes" % busId, "Wanted at t + %d" % offset)
            while True:
                if (baseT + offset) % busFreq == 0:
                    # Bus will be there on time.
                    break
                else:
                    print("Trying", baseT)
                    baseT += incrT
            incrT *= busFreq

        print("Part 2:", baseT, incrT)


part1()
part2()
