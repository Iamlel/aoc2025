import math

total = 0
with open("input.txt", "r") as fp:
    for pair in fp.readline().split(','):
        small, big = map(int, pair.split('-'))

        small = max(10, small)
        big = max(10, big)

        unique = set()
        for currentDigits in range(int(math.log10(small)) + 1, int(math.log10(big)) + 2):
            for digitCount in range(1, currentDigits):
                if (currentDigits % digitCount):
                    continue

                m = (10 ** currentDigits - 1) // (10 ** digitCount - 1)
                for i in range(max(10 ** (digitCount - 1), (small - 1) // m + 1), min(10 ** digitCount - 1, big // m) + 1):
                    unique.add(i * m)
        total += sum(unique)

print(total)