import math

total = 0
with open("input.txt", "r") as fp:
    for pair in fp.readline().split(','):
        small, big = map(int, pair.split('-'))
    
        digitsSmall = int(math.log10(small)) + 1
        if (digitsSmall % 2):
            small = 10 ** digitsSmall
            digitsSmall += 1
        
        digitsBig = int(math.log10(big)) + 1
        if (digitsBig % 2):
            digitsBig -= 1
            big = 10 ** digitsBig - 1
    
        for currentDigits in range(digitsSmall >> 1, (digitsBig >> 1) + 1):
            m = 10 ** currentDigits + 1
            newSmall = max(10 ** (currentDigits - 1), (small - 1) // m + 1)
            newBig = min(10 ** currentDigits - 1, big // m)
            total += (newBig - newSmall + 1) * m * (newBig + newSmall) >> 1

print(total)