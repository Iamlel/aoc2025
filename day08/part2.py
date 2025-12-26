from itertools import combinations
import math

with open("input.txt", "r") as fp:
    coordinates = [tuple(int(num) for num in line.strip().split(",")) for line in fp.readlines()]
    distances = [((a, b), math.hypot(b[0]-a[0], b[1]-a[1], b[2]-a[2])) for a, b in combinations(coordinates, 2)]

    circuits = []
    for (a, b), d in sorted(distances, key=lambda x: x[1]):
        ai = next((i for i, s in enumerate(circuits) if a in s), None)
        bi = next((i for i, s in enumerate(circuits) if b in s), None)

        if (ai == None):
            if (bi == None):
                circuits.append({a, b})
            else:
                circuits[bi].add(a)
        elif (bi == None):
            circuits[ai].add(b)
        elif (ai != bi):
            circuits[ai] |= circuits[bi]
            circuits.pop(bi)

        if (len(circuits) == 1 and len(circuits[0]) == len(coordinates)):
            print(a[0] * b[0])
            break