
def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        doorKey = int(lines[0])
        cardKey = int(lines[1])

        # From the sample data
        # doorKey = 17807724
        # cardKey = 5764801


        subject = 7

        v = 1
        for loopSize in range(20000000):
            if loopSize % 1000000 == 0:
                print("Iterated through", loopSize)
            if v == doorKey:
                doorLoopSize = loopSize
                print("Door loop size", doorLoopSize)
                # This break is here because I know door loop size is larger than card loop size.
                break
            if v == cardKey:
                cardLoopSize = loopSize
                print("Card loop size", cardLoopSize)
            v *= subject
            v %= 20201227

        # Now calculate the encryption code.

        # cardLoopSize is the smaller number so use that.
        v = 1
        subject = doorKey
        for _ in range(cardLoopSize):
            v *= subject
            v %= 20201227
        encryption = v
        print(encryption)

        # Now confirm by doing the other way
        v = 1
        subject = cardKey
        for _ in range(doorLoopSize):
            v *= subject
            v %= 20201227
        print(v)

part1()
