with open('input.txt') as fp:
    lines = fp.read().split()


def part1():
    twoCount = 0
    threeCount = 0
    for line in lines:
        hasTwo = 0
        hasThree = 0
        for unique in set(line):
            if list(line).count(unique) == 3:
                hasThree = 1
            elif list(line).count(unique) == 2:
                hasTwo = 1
        twoCount += hasTwo
        threeCount += hasThree
    return twoCount * threeCount


def part2():

    return 0


print(str(part1()))
