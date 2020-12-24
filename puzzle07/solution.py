
class Graph(object):

    def __init__(self):
        self.nodes = {}

    def add(self, name):
        if name not in self.nodes:
            self.nodes[name] = GraphNode(name)
        return self.nodes[name]

    def get(self, name):
        return self.nodes[name]


class GraphNode(object):

    def __init__(self, name):
        self.parents = {}
        self.children = {}
        self.name = name
        self.data = {}

    def add(self, node):
        self.children[node.name] = node
        node.parents[self.name] = self

    def addData(self, key, val):
        self.data[key] = val

    def __str__(self):
        return "%s %s" % (self.name, [n for n in self.children])

def part1():
    with open('input') as f:
        lines = f.readlines()

        g = Graph()
        for l in lines:
            l = l.rstrip()

            (outer, inners) = l.split(" contain ")
            p = outer.split(" ")
            print(p[0], p[1], p[2])
            node = g.add("%s-%s" % (p[0], p[1]))
            innerBags = inners.split(", ")
            for bag in innerBags:
                p = bag.split(" ")
                print(p[0], p[1], p[2])
                if p[0] == 'no':
                     break
                n2 = g.add("%s-%s" % (p[1], p[2]))
                node.addData("%s-%s" % (p[1], p[2]), int(p[0]))
                node.add(n2)

        for name, node in g.nodes.items():
            print(node)

        goldBag = g.get("shiny-gold")
        print(goldBag)

        visited = {}
        current = goldBag.parents
        while current:
            next = []
            for n in current:
                if n in visited:
                    continue
                visited[n] = True
                next += g.get(n).parents
            current = next

        print(visited)
        print(len(g.nodes))
        print(len(visited))

        def bagCount(n):
            if 'totalBags' in n.data:
                return n.data['totalBags']
            # Start with one for this bag.
            sum = 1
            for k, v in n.data.items():
                print(k)
                sum += v * bagCount(g.get(k))

            # Cache the number of total bags so its not recalculated each time.
            n.addData('totalBags', sum)
            return sum

        print("Part 2:", bagCount(goldBag) - 1)
        # 8867 was too low

part1()
