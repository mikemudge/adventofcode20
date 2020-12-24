def isValid(numbers, val):
    m = {}
    for n in numbers:
        if val - n in m:
            # print(val, n, val - n)
            return True
        m[n] = True
    return False


def part1():
    with open('input') as f:
        lines = f.readlines()

        numbers = []
        for i in range(25):
            numbers.append(int(lines[i]))

        print(numbers)

        valid = 0
        for i in range(25, len(lines)):
            v = int(lines[i])
            # Validate?
            if isValid(numbers, v):
                valid += 1
            else:
                print("Invalid ", v)
                print(numbers)

            numbers = numbers[1:] + [v]

        print("Part 1:", valid)


def part2():
    with open('input') as f:
        lines = f.readlines()

        # Result of part 1
        number = 69316178

        numbers = []
        for line in lines:
            numbers.append(int(line))
        start = 0
        tot = 0
        for end, v in enumerate(numbers):
            tot += v

            while tot > number:
                tot -= numbers[start]
                start += 1

            if start != end and tot == number:
                range = numbers[start:end]
                print(start, end, range)
                result = max(range) + min(range)
                print("Part 2:", result)


part1()
part2()