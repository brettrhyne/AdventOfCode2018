import sys

fout = open('output.txt', 'w')
sys.stdout = fout

with open('input.txt') as fp:
    freqs = [0]
    freq = 0
    loops = 0
    duplicateFound = False

    while not duplicateFound:
        for line in fp:
            # print(line, end='')
            freq += int(line)
            # print('freq = ' + str(freq))
            # print('freqs: ' + str(freqs[:]))
            if freq in freqs:
                duplicateFound = True
                print('duplicate: ' + str(freq))
                break
            else:
                freqs.append(freq)
        fp.seek(0)
        loops += 1
        print(str(loops))

fout.close()
