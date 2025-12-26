from itertools import combinations
import math, heapq, numpy

with open("input.txt", "r") as fp:
    distances = []
    for a, b in combinations([tuple(int(num) for num in line.strip().split(",")) for line in fp.readlines()], 2):
        distances.append(((a, b), math.hypot(b[0]-a[0], b[1]-a[1], b[2]-a[2])))

    circuits = []
    for (a, b), d in heapq.nsmallest(1000, distances, key=lambda x: x[1]):
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
    
print(numpy.prod(heapq.nlargest(3, [len(c) for c in circuits])))