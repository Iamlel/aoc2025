import re

with open("input.txt", "r") as fp:
    indices = iter([m.start() for m in re.finditer(r"[S^]", line)] for i, line in enumerate(fp.readlines()) if (i % 2 == 0))
    current = {next(indices)[0]: 1}
    for i in indices:
        for x in i:
            if (x in current):
                current[x - 1] = current.get(x - 1, 0) + current[x]
                current[x + 1] = current.get(x + 1, 0) + current[x]
                current.pop(x)
    
print(sum(current.values()))