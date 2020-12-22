import collections

def part1():
    with open('input') as f:
        lines = f.readlines()

        s = 0
        counts = collections.Counter()
        for l in lines:
            l = l.rstrip()
            if len(l) > 0:
                counts.update(l)
                continue

            s += len(counts)
            counts = collections.Counter()
        s += len(counts)

        print("Part 1:", s)

def part2():
    with open('input') as f:
        lines = f.readlines()

        s = 0
        counts = collections.Counter()
        people = 0
        for l in lines:
            l = l.rstrip()
            if len(l) > 0:
                people += 1
                counts.update(l)
                continue

            print('group', people, counts)
            for x in counts:
                if counts[x] == people:
                    s += 1
            people = 0
            counts = collections.Counter()
        for x in counts:
            if counts[x] == people:
                s += 1

        print("Part 2:", s)


part1()
part2()
