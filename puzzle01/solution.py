
def part1():
    with open('input') as f:
        lines = f.readlines()

        nums = ([False] * 2020)
        for l in lines:
            idx = int(l)
            nums[idx] = True

            if nums[2020 - idx]:
                print(idx, 2020 - idx, (2020 - idx) * idx)

def part2():
    with open('input') as f:
        lines = f.readlines()

        for l2 in lines:
            val = int(l2)
            # base is the number we need 2 of the other numbers to sum to.
            base = 2020 - val
            nums = ([False] * base)
            for l in lines:
                idx = int(l)
                if idx >= base:
                    continue
                nums[idx] = True

                if nums[base - idx]:
                    print(val, idx, base - idx, val * idx * (base - idx))


part1()
part2()