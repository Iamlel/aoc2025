total = 0
with open("input.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()

        voltages = [0] * 12
        for i, ch in enumerate(line):
            for e, v in enumerate(voltages):
                if (int(ch) > v and len(voltages) - e <= len(line) - i):
                    voltages[e] = int(ch)
                    voltages[e+1:] = [0] * (len(voltages) - e - 1)
                    break

        total += int(''.join([str(v) for v in voltages]))
print(total)