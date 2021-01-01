def parseTicket(line):
    return list(map(int, line.split(',')))


def invalidFields(ticket, crit):
    s = 0
    foundInvalid = False
    for n in ticket:
        if not checkValidValue(n, crit):
            foundInvalid = True
            s += n
    if foundInvalid:
        return s
    else:
        return None


def checkValidValue(n, crit):
    for name, critList in crit.items():
        for c in critList:
            if c['min'] <= n <= c['max']:
                print("Valid for ", name, c["min"], n, c["max"])
                return True

    print("Invalid for all fields", n)
    return False

def isValid(n, critList):
    for c in critList:
        if c['min'] <= n <= c['max']:
            return True
    # Did not meet any of the criteria.
    return False

def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        i = 0
        line = lines[i]
        crits = {}
        while len(line) > 0:
            print(len(line))
            name, criteria = line.split(": ")
            crit = criteria.split(" or ")
            print(name, crit)
            cs = []
            for c in crit:
                min, max = c.split("-")
                cs.append({
                    'min': int(min),
                    'max': int(max)
                })

            crits[name] = cs

            i += 1
            line = lines[i]

        # Move to the next section which is your ticket.
        # Skip blank line, and "Your ticket" line.
        i += 2
        yours = parseTicket(lines[i])
        print(yours)

        # Skip your ticket values, the blank line and "nearby tickets"
        i += 3
        invalid = 0
        validTickets = {}
        while i < len(lines):
            other = parseTicket(lines[i])
            print("Ticket", i, "values =", other)
            tmp = invalidFields(other, crits)
            if tmp is None:
                validTickets[i] = other
            else:
                invalid += tmp

            i += 1

        print("Part 1:", invalid)

        # Figure out which crit matches which value.
        possibles = {}
        for name, critList in crits.items():
            cols = []
            for col in range(len(yours)):
                validCol = True
                if col == 1 or col == 6:
                    verbose = True
                else:
                    verbose = False
                for identifier, t in validTickets.items():
                    n = t[col]
                    if not isValid(n, critList):
                        if verbose:
                            print(n, "not valid for", name, "in ticket", identifier)
                        validCol = False
                        break
                if validCol:
                    cols.append(col)

            print(name, "could be in col", cols)
            possibles[name] = cols


        print("There are x columns", len(possibles))

        mapping = {}
        numToField = [None] * 20
        while(True):
            n = None
            for name, p in possibles.items():
                if len(p) == 1:
                    print("Remove", name, "which must be col", p[0])
                    mapping[name] = p[0]
                    numToField[p[0]] = name
                    n = p[0]
                    possibles.pop(name)
                    break
            if n is None:
                print("Failed to find a column mapping in", possibles)
                break
            for name, p in possibles.items():
                if n in p:
                    p.remove(n)

        print("Final mapping", mapping)
        print("Reverse", numToField)


        part2 = 1
        part2 *= yours[mapping['departure time']]
        part2 *= yours[mapping['departure track']]
        part2 *= yours[mapping['departure station']]
        part2 *= yours[mapping['departure date']]
        part2 *= yours[mapping['departure location']]
        part2 *= yours[mapping['departure platform']]

        print("Part2:", part2)


part1()

