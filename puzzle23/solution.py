class Node:
    def __init__(self, data):
        self.data = data
        self.clockwise = None
        self.anticlockwise = None

    def __repr__(self):
        return self.data

    def toString(self, num):
        if num == 0:
            return ""
        return str(self.data) + " " + self.clockwise.toString(num - 1)


def part1():
    input = "398254716"

    # sample input
    # input = "389125467"

    cups = []
    for c in input:
        n = Node(int(c))
        cups.append(n)

    currentCup = cups[0]
    cupcount = len(cups)

    for i in range(cupcount):
        prev = cups[i]
        n = cups[(i + 1) % cupcount]
        next = cups[(i + 2) % cupcount]
        n.anticlockwise = prev
        n.clockwise = next

    for i in range(100):
        print("move %d" % (i + 1))
        print("cups: (%d) %s" % (currentCup.data, currentCup.clockwise.toString(cupcount - 1)))
        print("pick up: %s" % currentCup.clockwise.toString(3))
        pickup = [
            currentCup.clockwise.data,
            currentCup.clockwise.clockwise.data,
            currentCup.clockwise.clockwise.clockwise.data
        ]
        dest = currentCup.data - 1
        if dest == 0:
            dest = cupcount
        while dest in pickup:
            dest -= 1
            if dest == 0:
                dest = cupcount
        print("destination: %d" % dest)

        move1 = currentCup.clockwise

        # TODO this could use a map for speed?
        destNode = currentCup
        while destNode.data != dest:
            destNode = destNode.clockwise

        move3 = move1.clockwise.clockwise
        firstAfter = move3.clockwise

        # Insert move1-move3 into destNode -> destNode.clockwise
        move3.clockwise = destNode.clockwise
        move3.clockwise.anticlockwise = move3
        destNode.clockwise = move1
        destNode.clockwise.anticlockwise = destNode

        # then close the gap where the moved nodes were before.
        currentCup.clockwise = firstAfter
        currentCup.clockwise.anticlockwise = currentCup

        # now move the current cup around once clockwise.
        currentCup = currentCup.clockwise

    cup1 = currentCup
    while cup1.data != 1:
        cup1 = cup1.clockwise
    print("Part 1:", cup1.clockwise.toString(8).replace(" ", ""))


def part2():
    input = "398254716"

    # sample input
    # input = "389125467"

    cups = []
    for c in input:
        cid = int(c)
        n = Node(cid)
        cups.append(n)

    for c in range(len(input) + 1, 1000000 + 1):
        n = Node(c)
        cups.append(n)

    currentCup = cups[0]
    cupcount = len(cups)

    for i in range(cupcount):
        prev = cups[i]
        n = cups[(i + 1) % cupcount]
        next = cups[(i + 2) % cupcount]
        n.anticlockwise = prev
        n.clockwise = next

    cupMap = [Node(0) for _ in range(cupcount + 1)]
    # Go through all the cups and put them in a map for lookup.
    c = currentCup
    for i in range(cupcount):
        c = c.clockwise
        cupMap[c.data] = c

    print("init complete")

    for i in range(10000000):
        verbose = i % 100000 == 0
        if verbose:
            print("move %d" % (i + 1))
            print("cups: (%d) %s" % (currentCup.data, currentCup.clockwise.toString(9)))
            print("pick up: %s" % currentCup.clockwise.toString(3))
        pickup = [
            currentCup.clockwise.data,
            currentCup.clockwise.clockwise.data,
            currentCup.clockwise.clockwise.clockwise.data
        ]
        dest = currentCup.data - 1
        if dest == 0:
            dest = cupcount
        while dest in pickup:
            dest -= 1
            if dest == 0:
                dest = cupcount
        if verbose:
            print("destination: %d" % dest)

        move1 = currentCup.clockwise

        destNode = cupMap[dest]
        while destNode.data != dest:
            destNode = destNode.clockwise

        move3 = move1.clockwise.clockwise
        firstAfter = move3.clockwise

        # Insert move1-move3 into destNode -> destNode.clockwise
        move3.clockwise = destNode.clockwise
        move3.clockwise.anticlockwise = move3
        destNode.clockwise = move1
        destNode.clockwise.anticlockwise = destNode

        # then close the gap where the moved nodes were before.
        currentCup.clockwise = firstAfter
        currentCup.clockwise.anticlockwise = currentCup

        # now move the current cup around once clockwise.
        currentCup = currentCup.clockwise

    cup1 = cupMap[1]
    print(cup1.data, cup1.clockwise.data, cup1.clockwise.clockwise.data)
    print("Part 2:", cup1.clockwise.data * cup1.clockwise.clockwise.data)


part1()
part2()
