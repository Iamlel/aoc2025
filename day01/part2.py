dial = 50
total = 0
with open("./input.txt", "r") as fp:
    for line in fp.readlines():
        number = (dial + int(line.replace("R", "").replace("L", "-")))
        if (number < 0):
            add = -number // 100
            if (dial != 0):
                total += 1
        else:
            add = number // 100

        dial = number % 100
        if (add == 0 and dial == 0):
            total += 1
        total += add
print(total)