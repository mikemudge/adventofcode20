
def part1():
    data = "13,16,0,12,15,1"
    # data = "0,3,6"
    numbers = list(map(int, data.split(",")))


    turn = 1
    ages = {}
    for n in numbers:
        print(turn, "say", n)
        ages[n] = turn
        turn += 1

    next = 0

    while turn < 30000001:
        say = next
        if turn % 100000 == 0:
            print(turn, "say", say)
        # Calculate the next number based on the current one.
        if say not in ages:
            next = 0
        else:
            # print("next based off", say, "on", turn, "last said", ages[say], "age", turn - ages[say])
            next = turn - ages[say]

        ages[say] = turn
        turn += 1

part1()
