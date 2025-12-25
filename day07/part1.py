import re

total = 0
with open("input.txt", "r") as fp:
    indices = iter({m.start() for m in re.finditer(r"[S^]", line)} for i, line in enumerate(fp.readlines()) if (i % 2 == 0))
    current = next(indices)
    for i in indices:
        spl = current & i
        total += len(spl)
        current = (current - spl) | {x for s in spl for x in (s - 1, s + 1)}
    
print(total)