
def maskVal(mask, val):
    binString = "%036s" % format(val, 'b')
    print(binString)
    print(mask)
    res = []
    for i in range(36):
        b = "0"
        if i < len(binString):
            b = '1' if binString[i] == '1' else '0'
        if mask[i] != "X":
            b = mask[i]
        res.append(b)

    bStr = "".join(res)
    print(bStr)
    print(int(bStr, 2))
    return int(bStr, 2)


def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        mem = {}
        for line in lines:
            words = line.split()
            if words[0] == "mask":
                # Skip the = in words[1]
                mask = words[2]
                print("Mask update", mask)
            else:
                tmp = words[0][:-1]
                memId = int(tmp[4:])
                val = int(words[2])
                print(memId, val)
                mem[memId] = maskVal(mask, val)
        result = 0
        for m in mem:
            result += mem[m]
        print("Part 1:", result)

def writeMem(mem, addr, val):

    try:
        idx = addr.index("X")
        writeMem(mem, addr[:idx] + "0" + addr[idx + 1:], val)
        writeMem(mem, addr[:idx] + "1" + addr[idx + 1:], val)
    except ValueError:
        memId = int(addr, 2)
        mem[memId] = val


def writeMemAddresses(mem, memId, mask, val):
    binString = "%036s" % format(memId, 'b')
    print(binString)
    print(mask)

    res = []
    xCount = 0
    for i in range(36):
        if mask[i] == "0":
            b = '1' if binString[i] == '1' else '0'
        elif mask[i] == "1":
            b = "1"
        else:
            b = "X"
            xCount += 1
        res.append(b)
    print("X count:", xCount)
    bStr = "".join(res)
    print(bStr)

    writeMem(mem, bStr, val)


def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        mem = {}
        for line in lines:
            words = line.split()
            if words[0] == "mask":
                # Skip the = in words[1]
                mask = words[2]
                print("Mask update", mask)
            else:
                tmp = words[0][:-1]
                memId = int(tmp[4:])
                val = int(words[2])
                print(memId, val)
                writeMemAddresses(mem, memId, mask, val)
        result = 0
        for m in mem:
            result += mem[m]
        print("Part 2:", result)

maskVal("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11)
maskVal("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 101)
maskVal("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 0)
part1()

mem = {}
writeMemAddresses(mem, 42, "000000000000000000000000000000X1001X", 100)
writeMemAddresses(mem, 26, "00000000000000000000000000000000X0XX", 1)
print(len(mem))
part2()
