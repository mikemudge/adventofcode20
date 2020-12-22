def part1():
    with open('input') as f:
        lines = f.readlines()

        currentPass = {}
        valid = 0
        for l in lines:
            l = l.rstrip()
            if len(l) > 1:
                data = l.split(' ')
                for d in data:
                    f, v = d.split(':')
                    currentPass[f] = v
                continue

            # Current passport is complete.
            print(currentPass, len(currentPass))
            if len(currentPass) == 8:
                valid += 1
            if len(currentPass) == 7 and not currentPass.get('cid'):
                valid += 1
            # reset the current pass
            currentPass = {}


        if len(currentPass) == 8:
            valid += 1
        if len(currentPass) == 7 and not currentPass.get('cid'):
            valid += 1
        # Current passport is complete.
        print(currentPass, len(currentPass))
        print("Part 1:", valid)


def isValid(p):
    for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not p.get(f):
            # print('missing f', f)
            return False
    print(p)
    byr = int(p.get('byr'))
    iyr = int(p.get('iyr'))
    eyr = int(p.get('eyr'))
    if byr < 1920 or byr > 2002:
        print('invalid byr', byr)
        return False
    if iyr < 2010 or iyr > 2020:
        print('invalid iyr', iyr)
        return False
    if eyr < 2020 or eyr > 2030:
        print('invalid eyr', eyr)
        return False

    hgt = int(p.get('hgt')[:-2])
    if p.get('hgt')[-2:] == 'cm':
        if hgt < 150 or hgt > 193:
            print('invalid hgt', hgt)
            return False
    else:
        if hgt < 59 or hgt > 76:
            print('invalid hgt', hgt)
            return False
    hcl = p.get('hcl')
    if hcl[0] != '#' or len(hcl) != 7:
        print('invalid hcl', hcl)
        return False
    try:
        int(hcl[1:7], 16)
    except ValueError:
        print('invalid hcl', hcl)
        return False
    ecl = p.get('ecl')
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('invalid ecl', ecl)
        return False
    pid = p.get('pid')
    if len(pid) != 9:
        print('invalid pid', pid, len(pid))
        return False
    try:
        int(pid)
    except ValueError:
        print('not int pid', pid)
        return False
    return True

def part2():
    with open('input') as f:
        lines = f.readlines()

        currentPass = {}
        valid = 0
        for l in lines:
            l = l.rstrip()
            if len(l) > 1:
                data = l.split(' ')
                for d in data:
                    f, v = d.split(':')
                    currentPass[f] = v
                continue

            # Current passport is complete.
            if isValid(currentPass):
                valid += 1
            # reset the current pass
            currentPass = {}


        if isValid(currentPass):
            valid += 1
        # Current passport is complete.
        print("Part 2:", valid)

part1()
part2()