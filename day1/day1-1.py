with open('input.txt') as fp:
    freq = 0
    for line in fp:
        print(line, end='')
        freq += int(line)
        print('freq = ' + str(freq))
