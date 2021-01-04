class Rule(object):
    def __init__(self, ruleId):
        self.ruleId = ruleId
        # Options is a list of OR based rules.
        # Each item is a ordered list of ruleId's which must match.
        self.options = []
        self.letter = None

    def set_letter(self, letter):
        self.letter = letter

    def add_option(self, ruleList):
        self.options.append(ruleList)

    def __str__(self):
        ruleStr = " | ".join([" ".join(o) for o in self.options])
        return "Rule %s: %s" % (self.ruleId, ruleStr)


def is_valid(r, rules, line, idx, verbose=False):
    if idx >= len(line):
        # the rules require more letters than we have.
        return False, idx

    if r.letter:
        valid = line[idx] == r.letter
        if valid:
            if verbose:
                print("%s matches %s" % (line[idx:idx + 1], r.ruleId))
            return True, idx + 1

    matchingRule = None
    for o in r.options:
        idx2 = idx
        match = True
        for p in o:
            subR = rules.get(p)
            valid, idx2 = is_valid(subR, rules, line, idx2)
            if not valid:
                match = False
                break
        if match:
            if matchingRule:
                print("Second match", idx2, matchingRule[1])
            matchingRule = o, idx2

    if matchingRule:
        if verbose:
            print("%s matches %s - %s" % (line[idx:matchingRule[1]], r.ruleId, " ".join(matchingRule[0])))
        return True, matchingRule[1]

    return False, idx

def parseRules(lines):
    rules = {}
    i = 0
    while(len(lines[i]) > 0):
        line = lines[i]
        ruleId, ruleStr = line.split(": ")
        r = Rule(ruleId)
        if ruleStr[0] == '"':
            print("Rule %s is letter: %s" % (ruleId, ruleStr))
            r.set_letter(ruleStr[1])
        else:
            options = ruleStr.split(" | ")
            for o in options:
                sub_rules = o.split(" ")
                # print("Adding option", " ".join(sub_rules))
                r.add_option(sub_rules)
        rules[ruleId] = r
        i += 1

    return rules, i


def part1():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        rules, i = parseRules(lines)

        # Skip the blank line.
        i += 1

        r0 = rules["0"]
        print(r0)

        # Now read the test strings
        testLines = lines[i:]

        print("Testing %d lines for matching" % len(testLines))

        # Iterate for part 1
        validCount = 0
        for line in testLines:
            valid, idx = is_valid(r0, rules, line, 0)
            if valid and idx == len(line):
                validCount += 1

        print("Part 1:", validCount)


def part2():
    with open('input') as f:
        lines = f.readlines()
        lines = [l.rstrip() for l in lines]

        rules, i = parseRules(lines)
        # Skip the blank line.
        i += 1

        # Update rules for part 2
        print(rules["8"])
        print(rules["11"])
        rules["8"].options = [["42"], ["42", "8"]]
        rules["11"].options = [["42", "31"], ["42", "11", "31"]]
        print(rules["8"])
        print(rules["11"])
        # for x in range(len(rules)):
        #     print("%d %s" % (x, rules[str(x)]))

        r0 = rules["0"]
        r42 = rules["42"]
        r31 = rules["31"]

        # 8 11
        # 8: 42 | 42 8
        # 11: 42 31 | 42 11 31
        # 42+ + 42 * x + 31 * x
        # Some number of 42's > 2 followed by some number of 31's < number of 42's
        # Minimal case 42, 42 31
        # With extra 8 would be 42 42, 42 31
        # With extra 11 would 42, 42 42 31 31

        # Now read the test strings
        testLines = lines[i:]

        # In the sample this is 5, but in my input its 8.
        len42 = 8

        validCount = 0
        for line in testLines:
            # print("Testing %s" % line)
            # match on 42 as many times as possible.
            match42count = 0
            valid = True
            idx = 0
            while valid:
                valid, idx = is_valid(r42, rules, line, idx)
                if valid:
                    match42count += 1

            if idx != len42 * match42count:
                print("Testing %s" % line)
                raise Exception("Unexepected idx after matching 42's")

            if match42count < 2:
                print("Testing %s" % line)
                print("Couldn't find enough 42's (%d), invalid string" % match42count)
                continue

            # print("Found %d 42's up to %d" % (match42count, idx))
            counted = False
            for idx2 in range(match42count * len42, len42, -len42):
                # print("start finding 31's at ", idx2)

                # next match 31's
                match31count = 0
                valid = True
                idx31 = idx2
                while valid:
                    valid, idx31 = is_valid(r31, rules, line, idx31)
                    if valid:
                        match31count += 1

                # print("Found %d 31's at %d:%d, line len = %d" % (match31count, idx2, idx31, len(line)))
                if match31count > 0 and match31count < match42count and idx31 == len(line):
                    # print("Counted", match42count, match31count)
                    validCount += 1
                    counted = True
                    # If we find a valid, count it and skip the rest.
                    break

            if not counted:
                print("Testing %s" % line)
                print("Found %d 42's up to %d" % (match42count, idx))
                print("Found %d 31's at %d:%d, line len = %d" % (match31count, idx2, idx31, len(line)))

            # if valid:
            #     break
        print("Part 2:", validCount)
        # 356 is too low :(
        # 357 is right, not sure which one I missed though???



part1()
part2()