from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.nodes = defaultdict(dict)

    def add(self, node1, node2):
        self.nodes[node1].update(node2)


def part1():
    with open('input') as f:
        lines = f.readlines()

        g = Graph()
        for l in lines:
            l = l.rstrip()

            (outer, inners) = l.split(" contain ")
            p = outer.split(" ")
            print(p[0], p[1], p[2])
            n1 = "%s-%s" % (p[0], p[1])
            innerBags = inners.split(", ")
            for bag in innerBags:
                p = bag.split(" ")
                print(p[0], p[1], p[2])
                if p[0] == 'no':
                     break
                n2 = "%s-%s" % (p[1], p[2])
                g.add(n1, {n2: p[0]})

        for name, node in g.nodes.items():
            print(name, node)

part1()
