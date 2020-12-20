
def part1():
    with open('input') as f:
        lines = f.readlines()

        valid = 0
        for l in lines:
            (crit, value) = l.split(': ')
            (nums, c) = crit.split(' ')
            low, high = nums.split('-')

            num = value.count(c)
            print(num)

            if int(low) <= num <= int(high):
                valid += 1
            else:
                print(low, high, c, value)


        print(valid)

def part2():
    with open('input') as f:
        lines = f.readlines()

        valid = 0
        for l in lines:
            (crit, value) = l.split(': ')
            (nums, c) = crit.split(' ')
            low, high = nums.split('-')

            # This is doing an XOR for the char in each location.
            if (value[int(low) - 1] == c) != (value[int(high) - 1] == c):
                valid += 1
            else:
                print(low, high, c, value)


        print(valid)


part1()
part2()