total = 0
with open("input.txt", "r") as fp:
    map = [list(line.strip()) for line in fp.readlines()]
    for y, line in enumerate(map):
        for x, ch in enumerate(line):
            if (map[y][x] == '.'):
                continue

            counter = 0
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if (dx + x < 0 or dx + x >= len(map[0]) or dy + y < 0 or dy + y >= len(map)):
                    continue
                if (map[dy + y][dx + x] == '@'):
                    counter += 1
            
            if (counter < 4):
                total += 1
print(total)