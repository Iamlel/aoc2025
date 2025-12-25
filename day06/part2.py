from itertools import chain
import re, numpy

class Operation:
    def __init__(self, start, group):
        self.i = start
        self.g = group

    def start(self):
        return self.i
    
    def group(self):
        return self.g

total = 0
with open("input.txt", "r") as fp:
    problems = [line.strip("\n") for line in fp.readlines()]
    operations = re.finditer(r"[+*]", problems[-1])
    prev = next(operations)
    
    # ideally you would iterate through and convert everything to my new Operation
    # but we don't care about safety
    # or you would just not use classes
    for op in chain(operations, [Operation(len(problems[-1]) + 1, None)]):
        numbers = numpy.zeros(op.start() - prev.start() - 1, dtype=int)
        for p in problems[:-1]:
            for i, digit in enumerate(p[prev.start():op.start() - 1]):
                if (digit != ' '):
                    numbers[i] *= 10
                    numbers[i] += int(digit)

        if (prev.group() == '*'):
            total += numpy.prod(numbers)
        else:
            total += numpy.sum(numbers)

        prev = op
print(total)