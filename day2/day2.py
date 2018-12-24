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


def part2NLogN():
    linesI = lines.copy()
    linesJ = lines.copy()
    for lineI in linesI:
        for lineJ in linesJ[1:]:
            if hasOneDifference(lineI, lineJ):
                return removeDifferentChar(lineI, lineJ)
        del linesJ[0]


def hasOneDifference(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    i = 0
    differences = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            differences += 1
        i += 1
    if differences == 1:
        return True
    else:
        return False



def removeDifferentChar(str1, str2):
    i = 0
    list1 = list(str1)
    list2 = list(str2)
    while True:
        if list1[i] != list2[i]:
            del list1[i]
            return ''.join(list1)
        else:
            i += 1


print('part 1: ' + str(part1()))
print('part 2: ' + part2NLogN())