import collections
import math

class Tile(object):
    def __init__(self, tid, lines):
        self.tid = tid
        self.lines = lines
        # TODO calculate edges?
        self.top = calculateBestId(self.getTop())
        self.bottom = calculateBestId(self.getBottom())
        self.left = calculateBestId(self.getLeft())
        self.right = calculateBestId(self.getRight())
        self.borders = [self.top, self.left, self.bottom, self.right]

    def getLeft(self):
        return "".join([l[0] for l in self.lines])

    def getRight(self):
        return "".join([l[len(self.lines[0]) - 1] for l in self.lines])

    def getTop(self):
        return self.lines[0]

    def getBottom(self):
        return self.lines[len(self.lines) - 1]

    def __str__(self):
        return "\n".join(self.lines)

    def otherTile(self, tiles):
        for t in tiles:
            if t != self:
                return t
        raise Exception("No other tile found %d" % len(tiles))

    def rotate(self):
        newlines = []
        for x in range(len(self.lines[0])):
            newlines.append("".join(self.lines[y][x] for y in range(len(self.lines) - 1, -1, -1)))
        self.lines = newlines
        tmp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = tmp
        return self

    def flipHorizontal(self):
        self.lines = [line[::-1] for line in self.lines]
        tmp = self.left
        self.left = self.right
        self.right = tmp

    def flipVertical(self):
        self.lines = list(reversed(self.lines))
        tmp = self.top
        self.top = self.bottom
        self.bottom = tmp

    def find(self, pattern):
        ph = len(pattern)
        pw = len(pattern[0])
        num = 0
        for y in range(len(self.lines) - ph):
            for x in range(len(self.lines[y]) - pw):
                # print("finding at %d,%d" % (x, y))
                match = True
                for py, pline in enumerate(pattern):
                    for px, c in enumerate(pline):
                        if c == "#" and self.lines[y + py][x + px] != "#":
                            match = False
                            break
                    if not match:
                        break
                if match:
                    num += 1
                    print("Found sea monster at %d, %d", (y, x))
                    # Can sea monsters overlap?
                    # TODO should we skip here?
                    for py, pline in enumerate(pattern):
                        replacement = []
                        for px, c in enumerate(pline):
                            if c == "#":
                                replacement.append("O")
                            else:
                                replacement.append(self.lines[y + py][x + px])
                        line = self.lines[y + py]
                        self.lines[y + py] = line[:x] + "".join(replacement) + line[x + pw:]
        return num

def calculateBestId(tiles):
    first = tiles[:]
    second = tiles[::-1]
    # Might need to reverse these so they match.
    if first < second:
        return first
    return second

def parseTiles(lines):
    tiles = {}
    tileId = None
    tileLines = []
    for line in lines:
        if len(line) < 1:
            # end of tile
            t = Tile(tileId, tileLines)
            tiles[tileId] = t
            tileId = None
            tileLines = []
            continue
        if "Tile" in line:
            tileId = int(line[5:len(line) - 1])
        else:
            tileLines.append(line)

    # make sure we get the last tile.
    t = Tile(tileId, tileLines)
    tiles[tileId] = t
    return tiles

def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        tiles = parseTiles(lines)

        # 144 -> 12 * 12?
        print(len(tiles))

        edges = collections.Counter()
        for tid, t in tiles.items():
            edges.update({t.left: 1, t.right: 1, t.top: 1, t.bottom: 1})

        print(edges)

        result = 1
        edgePieces = []
        cornerPieces = []
        middlePieces = []
        for tid, t in tiles.items():
            unmatched = 0
            for b in t.borders:
                if edges[b] == 1:
                    unmatched += 1
            if unmatched == 0:
                middlePieces.append(t)
            elif unmatched == 1:
                edgePieces.append(t)
            elif unmatched == 2:
                cornerPieces.append(t)
            else:
                raise("Piece doesn't match enough sides")
        for c in cornerPieces:
            result *= c.tid

        print("Part 1:", result, len(edgePieces), len(cornerPieces))
        # print("Part 1:", result, 40, 4)

def part2():
    seaMonster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        tiles = parseTiles(lines)

        tileMap = collections.defaultdict(list)
        for tid, t in tiles.items():
            # add edge
            tileMap[t.left].append(t)
            tileMap[t.top].append(t)
            tileMap[t.right].append(t)
            tileMap[t.bottom].append(t)

        for tid, t in tiles.items():
            unmatched = 0
            for b in t.borders:
                if len(tileMap[b]) == 1:
                    unmatched += 1
            if unmatched == 2:
                print("Tile %s" % t.tid)
                print(t.left, len(tileMap[t.left]))
                print(t.right, len(tileMap[t.right]))
                print(t.top, len(tileMap[t.top]))
                print(t.bottom, len(tileMap[t.bottom]))

        size = int(math.sqrt(len(tiles)))
        print("Assigning tiles to a %dx%d grid" % (size, size))
        grid = [[Tile("None", ["0"])] * size for _ in range(size)]

        # From above output we will start with Tile 2971 which is a corner piece in the top left.
        if 2971 in tiles:
            # sample
            start = tiles[2971]
        else:
            # real
            start = tiles[1543]
        grid[0][0] = start

        for y in range(size):
            if y > 0:
                # assign based on above.
                above = grid[y - 1][0]
                edge = above.bottom
                if len(tileMap[edge]) == 1:
                    print("Nothing matches at %d, %d" % (x, y))
                    break
                t = above.otherTile(tileMap[edge])
                # TODO rotate this?
                if t.top == edge:
                    # rotation not required
                    pass
                elif t.right == edge:
                    t.rotate().rotate().rotate()
                elif t.bottom == edge:
                    t.rotate().rotate()
                elif t.left == edge:
                    t.rotate()

                if above.getBottom() != t.getTop():
                    # flip?
                    t.flipHorizontal()
                grid[y][0] = t

            for x in range(size):
                if x > 0:
                    left = grid[y][x - 1]
                    edge = left.right
                    if len(tileMap[edge]) == 1:
                        print("Nothing matches at %d, %d" % (x, y))
                        break
                    t = left.otherTile(tileMap[edge])
                    if t.left == edge:
                        # rotation not required
                        pass
                    elif t.top == edge:
                        t.rotate().rotate().rotate()
                    elif t.right == edge:
                        t.rotate().rotate()
                    elif t.bottom == edge:
                        t.rotate()

                    if left.getRight() != t.getLeft():
                        # flip?
                        t.flipVertical()
                    grid[y][x] = t

        for y in range(size):
            for i in range(10):
                print(" ".join(grid[y][x].lines[i] for x in range(size)))
            print("")

        bigPictureLines = []
        for y in range(size):
            # remove the borders.
            for i in range(1, 9):
                # remove the borders
                l = "".join(grid[y][x].lines[i][1:-1] for x in range(size))
                bigPictureLines.append(l)
        bigPicture = Tile("Big Picture", bigPictureLines)

        # discovered by trial and error that rotating twice finds sea monsters.
        bigPicture.rotate().rotate()
        print(bigPicture)

        num = bigPicture.find(seaMonster)

        print(bigPicture)

        print("Found %d in rotated" % num)

        rough = 0
        for y in range(len(bigPicture.lines)):
            for x in range(len(bigPicture.lines[y])):
                if bigPicture.lines[y][x] == "#":
                    rough += 1

        print("Part 2:", rough)

part1()
part2()