with open('input.txt') as fp:
    lines = list(fp.read().split())


def part1():
    return sum(map(int, lines))


def part2():
    freq = 0
    seen = {freq}

    while True:
        for line in lines:
            freq += int(line)
            if freq in seen:
                return freq
            else:
                seen.add(freq)


print('part 1: ' + str(part1()))
print('part 2: ' + str(part2()))
