import re

total = 0
with open("input.txt", "r") as fp:
    problems = [re.split(r"\s+", line.strip()) for line in fp.readlines()]
    for i in range(len(problems[0])):
        if (problems[-1][i] == '*'):
            subtotal = 1
            for p in problems[:-1]:
                subtotal *= int(p[i])
            total += subtotal
        else:
            total += sum(int(p[i]) for p in problems[:-1])
print(total)