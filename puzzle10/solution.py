
def part1():
    with open('input') as f:
        lines = f.readlines()

        joltages = []
        for l in lines:
            joltages.append(int(l))

        joltages = sorted(joltages)
        print(joltages)

        lastj = 0
        # Includes the diff from the highest to the inbuilt which is always 3
        diffs = {1: 0, 2: 0, 3: 1}
        for j in joltages:
            diffs[j - lastj] += 1
            lastj = j

        print("Part 1:", diffs[1] * diffs[3])


def part2():
    with open('input') as f:
        lines = f.readlines()

        joltages = []
        for l in lines:
            joltages.append(int(l))

        joltages = sorted(joltages)
        print(joltages)
        cache = {0: 1}

        for j in joltages:
            v = 0
            if j > 0:
                v += cache.get(j - 1, 0)
            if j > 1:
                v += cache.get(j - 2, 0)
            if j > 2:
                v += cache.get(j - 3, 0)
            cache[j] = v

        print(cache)

part1()
part2()