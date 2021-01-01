
def part1():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        dir = 1
        x = 0
        y = 0
        for line in lines:
            op = line[0]
            dis = int(line[1:])

            print(op, dis)

            if op == 'N':
                y += dis
            elif op == 'S':
                y -= dis
            elif op == 'E':
                x += dis
            elif op == 'W':
                x -= dis
            elif op == 'L':
                dis = dis / 90
                dir = (dir + 4 - dis) % 4
            elif op == 'R':
                dis = dis / 90
                dir = (dir + dis) % 4
            elif op == 'F':
                if dir == 0:
                    y += dis
                elif dir == 2:
                    y -= dis
                elif dir == 1:
                    x += dis
                elif dir == 3:
                    x -= dis
                else:
                    raise Exception('unknown dir %d' % dir)
            else:
                raise Exception('unknown op %s' % op)
        print(x,y)
        print("Part 1: ", abs(x) + abs(y))
        # 1746 is too high.

def part2():
    with open('input') as f:
        lines = f.readlines()

        lines = [l.rstrip() for l in lines]

        x = 0
        y = 0
        # wx, wy is the waypoints location relative to the ship.
        wx = 10
        wy = 1
        for line in lines:
            op = line[0]
            dis = int(line[1:])

            print(x, y, wx, wy, op, dis)

            if op == 'N':
                wy += dis
            elif op == 'S':
                wy -= dis
            elif op == 'E':
                wx += dis
            elif op == 'W':
                wx -= dis
            elif op == 'L':
                dis = int(dis / 90)
                for i in range(dis):
                    tmp = wx
                    wx = -wy
                    wy = tmp
            elif op == 'R':
                dis = int(dis / 90)
                for i in range(dis):
                    tmp = wy
                    wy = -wx
                    wx = tmp
            elif op == 'F':
                y += wy * dis
                x += wx * dis
            else:
                raise Exception('unknown op %s' % op)
        print(x,y)
        print("Part 1: ", abs(x) + abs(y))
        # 1746 is too high.

part1()
part2()
