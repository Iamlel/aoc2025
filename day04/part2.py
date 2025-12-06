import queue

total = 0
with open("input.txt", "r") as fp:
    map = []
    q = queue.SimpleQueue()

    for y, line in enumerate(fp.readlines()):
        mlist = []
        for x, ch in enumerate(line.strip()):
            mlist.append(ch)
            if (ch == '@'):
                q.put((x, y))
        map.append(mlist.copy())
    
    lastLength = 0
    while (lastLength != q.qsize()):
        lastLength = q.qsize()
        for x in range(lastLength):
            node = q.get()
            counter = 0
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if (dx + node[0] < 0 or dx + node[0] >= len(map[0]) or dy + node[1] < 0 or dy + node[1] >= len(map)):
                    continue
                if (map[dy + node[1]][dx + node[0]] == '@'):
                    counter += 1

                if (counter > 3):
                    break
            else:
                total += 1
                map[node[1]][node[0]] = '.'
                continue

            q.put(node)
    
print(total)