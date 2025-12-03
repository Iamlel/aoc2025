total = 0
with open("input.txt", "r") as fp:
    for line in fp.readlines():
        x, y = 0, 0
        for i, ch in enumerate(line.strip()):
            if (int(ch) > x and i != len(line) - 2): # last char
                x = int(ch)
                y = 0
            else:
                y = max(y, int(ch))
        total += x * 10 + y
print(total)