def traverseSlope(vy, vx, grid):
    trees = 0
    for y in range(0, len(grid), vy):
        x = ((y / vy) * vx) % len(grid[0])

        if grid[y][x] == '#':
            trees += 1

    return trees

def part1():
    with open('input') as f:
        lines = f.readlines()

        grid = []
        for l in lines:
            grid.append(l.rstrip())

        print(grid)

        trees = traverseSlope(1, 3, grid)
        print(trees)


def part2():
    with open('input') as f:
        lines = f.readlines()

        grid = []
        for l in lines:
            grid.append(l.rstrip())

        print(grid)

        total = 1
        trees = traverseSlope(1, 1, grid)
        total *= trees
        print(trees)
        trees = traverseSlope(1, 3, grid)
        total *= trees
        print(trees)
        trees = traverseSlope(1, 5, grid)
        total *= trees
        print(trees)
        trees = traverseSlope(1, 7, grid)
        total *= trees
        print(trees)
        trees = traverseSlope(2, 1, grid)
        total *= trees
        print(trees)

        print("Part 2:", total)
        # 2981784960 is too low


part1()
part2()
